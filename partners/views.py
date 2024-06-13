from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Partners, ProductInfo, CaseStudy
from .forms import PartnerForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import logging

logger = logging.getLogger(__name__)

class PartnerDetailView(DetailView):
    model = Partners
    template_name = 'partner_detail.html'
    context_object_name = 'partner'


class IndexView(TemplateView):
    template_name = 'index.html'


class PartnerListView(ListView):
    model = Partners
    template_name = 'partner_list.html'
    context_object_name = 'partners'

    def get_queryset(self):
        return Partners.objects.prefetch_related(
            'service_content',
            'ai_category',
            'cost',
            'product_info',
            'case_study'
        ).all()

# CreateViewを継承 Partnersオブジェクトの作成を処理
class PartnerCreateView(CreateView):
    model = Partners
    form_class = PartnerForm
    template_name = 'partner_form.html'
    success_url = reverse_lazy('partners:index')

    # postメソッド POSTリクエストが送信の際に呼び出される
    # 各メソッドの分岐
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid() and 'confirm' in request.POST:
            return self.form_confirm(form)
        elif form.is_valid() and 'finalize' in request.POST:
            return self.form_finalize(form)
        elif 'back' in request.POST:
            return self.form_invalid(form)
        else:
            return self.form_invalid(form)

    # form_confilmメソッド、フォームデータを確認するための一時保存
    def form_confirm(self, form):
        # フォームからファイルを所得
        logo = self.request.FILES.get('logo') if 'logo' in self.request.FILES else form.instance.logo
        product_info_image = self.request.FILES.get('product_info_image')
        case_study_image = self.request.FILES.get('case_study_image')

        # 画像ファイルを一時保存してURLを取得
        logo_url = self._save_temp_image(logo) if logo else None
        product_info_image_url = self._save_temp_image(product_info_image) if product_info_image else None
        case_study_image_url = self._save_temp_image(case_study_image) if case_study_image else None

        logger.debug("Logo URL: %s", logo_url)
        logger.debug("Product Info Image URL: %s", product_info_image_url)
        logger.debug("Case Study Image URL: %s", case_study_image_url)

        return render(self.request, 'partner_confirm.html', {
            'form': form,
            'logo_url': logo_url,
            'product_info_name': self.request.POST.get('product_info_name', ''),
            'product_info_content': self.request.POST.get('product_info_content', ''),
            'product_info_image_url': product_info_image_url,
            'case_study_name': self.request.POST.get('case_study_name', ''),
            'case_study_content': self.request.POST.get('case_study_content', ''),
            'case_study_image_url': case_study_image_url,
        })

    def _save_temp_image(self, image):
        # 一時ファイルを保存し、そのURLを返す
        path = default_storage.save('tmp/' + image.name, ContentFile(image.read()))
        return default_storage.url(path)

    # form_finalizeメソッド　フォームデータをデータベースに最終的に保存
    def form_finalize(self, form):
        self.object = form.save()

        # product_info と case_study の関連つけられた、Partnersインスタンスに保存します
        product_info_name = self.request.POST.get('product_info_name')
        product_info_content = self.request.POST.get('product_info_content')
        product_info_image = self.request.FILES.get('product_info_image')
        case_study_name = self.request.POST.get('case_study_name')
        case_study_content = self.request.POST.get('case_study_content')
        case_study_image = self.request.FILES.get('case_study_image')

        if product_info_name and product_info_content:
            product_info = ProductInfo(
                partner=self.object,
                name=product_info_name,
                content=product_info_content,
                image=product_info_image
            )
            product_info.save()

        if case_study_name and case_study_content:
            case_study = CaseStudy(
                partner=self.object,
                name=case_study_name,
                content=case_study_content,
                image=case_study_image
            )
            case_study.save()

        return redirect(self.success_url)

    # form_validメソッド formが有効な時にform_confirmメソッドを呼び出す
    def form_valid(self, form):
        return self.form_confirm(form)

    # form_validメソッド formが有効な時にform_confirmメソッドを呼び出す
    def form_valid(self, form):
        return self.form_confirm(form)

    # form_invalidメソッド formが無効な場合にカスタム処理して、コンテキストを更新して、テンプレートをレンダリングする
    def form_invalid(self, form):
        logger.debug("form_invalid called")
        # form_invalidのカスタム処理
        context = self.get_context_data(form=form)
        context.update({
            'logo_url': self.request.POST.get('logo_url', ''),
            'product_info_name': self.request.POST.get('product_info_name', ''),
            'product_info_content': self.request.POST.get('product_info_content', ''),
            'product_info_image_url': self.request.POST.get('product_info_image_url', ''),
            'case_study_name': self.request.POST.get('case_study_name', ''),
            'case_study_content': self.request.POST.get('case_study_content', ''),
            'case_study_image_url': self.request.POST.get('case_study_image_url', ''),
        })
        context['object'] = None  # self.objectがない場合でもエラーを回避するためにNoneを設定
        logger.debug("Context prepared: %s", context)
        return self.render_to_response(context)



