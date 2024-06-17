from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Partners, ProductInfo, CaseStudy, ServiceContent, AiCategory, Cost
from .forms import PartnerForm, PartnerSearchForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import logging

logger = logging.getLogger(__name__)

class PartnerDetailView(DetailView):
    """
    パートナーの詳細ビューを表示するクラス。
    """
    model = Partners  # モデルを指定
    template_name = 'partner_detail.html'  # テンプレートファイルを指定
    context_object_name = 'partner'  # テンプレート内で使用するコンテキスト名を指定

    def get_queryset(self):
        """
        関連するデータを事前に取得するためのクエリセットを返す。
        """
        return Partners.objects.prefetch_related(
            'service_content',
            'ai_category',
            'cost',
            'product_info',
            'case_study',
        )

    def get_context_data(self, **kwargs):
        """
        テンプレートに渡すコンテキストデータを追加する。
        """
        context = super().get_context_data(**kwargs)
        context['service_content'] = self.object.service_content.all()  # サービスコンテンツを追加
        context['ai_category'] = self.object.ai_category.all()  # AIカテゴリを追加
        context['cost'] = self.object.cost.all()  # コスト情報を追加
        context['product_info']= self.object.product_info.all() #製品情報を追加
        context['case_study']= self.object.case_study.all() #事例を追加
        print(f"Service content: {context['service_content']}")
        print(f"AI category: {context['ai_category']}")
        print(f"Cost: {context['cost']}")
        print(f"Product info: {context['product_info']}")
        print(f"Case study: {context['case_study']}")
        return context


class IndexView(TemplateView):
    """
    インデックスビューを表示するクラス。
    """
    template_name = 'index.html'  # テンプレートファイルを指定


class PartnerListView(ListView):
    """
    パートナー一覧ビューを表示するクラス。
    """
    model = Partners  # モデルを指定
    template_name = 'partner_list.html'  # テンプレートファイルを指定
    context_object_name = 'partners'  # テンプレート内で使用するコンテキスト名を指定

    def get_queryset(self):
        """
        一覧表示するためのクエリセットを返す。
        """
        queryset = Partners.objects.prefetch_related(
            'service_content',
            'ai_category',
            'cost',
            'product_info',
            'case_study'
        ).all()

        form = PartnerSearchForm(self.request.GET or None)
        if form.is_valid():
            if form.cleaned_data['service_content']:
                queryset = queryset.filter(service_content=form.cleaned_data['service_content'])
            if form.cleaned_data['ai_category']:
                queryset = queryset.filter(ai_category=form.cleaned_data['ai_category'])
            if form.cleaned_data['cost']:
                queryset = queryset.filter(cost=form.cleaned_data['cost'])

        return queryset

    def get_context_data(self, **kwargs):
        """
        テンプレートに渡すコンテキストデータを追加する。
        """
        context = super().get_context_data(**kwargs)
        context['all_services'] = ServiceContent.objects.all()  # 全サービスコンテンツを追加
        context['all_categories'] = AiCategory.objects.all()  # 全AIカテゴリを追加
        context['all_costs'] = Cost.objects.all()  # 全コスト情報を追加
        context['form'] = PartnerSearchForm(self.request.GET or None)  # 検索フォームを追加
        return context


class PartnerCreateView(CreateView):
    """
    パートナー作成ビューを表示するクラス。
    """
    model = Partners  # モデルを指定
    form_class = PartnerForm  # 使用するフォームクラスを指定
    template_name = 'partner_form.html'  # テンプレートファイルを指定
    success_url = reverse_lazy('partners:index')  # 成功時のリダイレクトURLを指定

    def post(self, request, *args, **kwargs):
        """
        POSTリクエストの処理を行う。
        """
        form = self.get_form()
        if form.is_valid() and 'confirm' in request.POST:
            return self.form_confirm(form)  # 確認処理
        elif form.is_valid() and 'finalize' in request.POST:
            return self.form_finalize(form)  # 最終処理
        elif 'back' in request.POST:
            return self.form_invalid(form)  # 無効なフォームの処理
        else:
            return self.form_invalid(form)

    def form_confirm(self, form):
        """
        確認ページを表示するための処理。
        """
        logo = self.request.FILES.get('logo') if 'logo' in self.request.FILES else form.instance.logo
        product_info_image = self.request.FILES.get('product_info_image')
        case_study_image = self.request.FILES.get('case_study_image')

        logo_url = self._save_temp_image(logo) if logo else None
        product_info_image_url = self._save_temp_image(product_info_image) if product_info_image else None
        case_study_image_url = self._save_temp_image(case_study_image) if case_study_image else None

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
        """
        一時的な画像を保存するための処理。
        """
        path = default_storage.save('tmp/' + image.name, ContentFile(image.read()))
        return default_storage.url(path)

    def form_finalize(self, form):
        """
        フォームの最終処理を行い、データベースに保存する。
        """
        self.object = form.save()

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

    def form_invalid(self, form):
        """
        無効なフォームを再表示する。
        """
        self.object = None
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
        return self.render_to_response(context)









