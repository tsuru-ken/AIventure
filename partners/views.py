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
        context = super().get_context_data(**kwargs)
        context['all_services'] = ServiceContent.objects.all()
        context['all_categories'] = AiCategory.objects.all()
        context['all_costs'] = Cost.objects.all()
        context['form'] = PartnerSearchForm(self.request.GET or None)
        return context

class PartnerCreateView(CreateView):
    model = Partners
    form_class = PartnerForm
    template_name = 'partner_form.html'
    success_url = reverse_lazy('partners:index')

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

    def form_confirm(self, form):
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
        path = default_storage.save('tmp/' + image.name, ContentFile(image.read()))
        return default_storage.url(path)

    def form_finalize(self, form):
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






