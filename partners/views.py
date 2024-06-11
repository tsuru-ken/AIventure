from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .models import Partners, ProductInfo, CaseStudy
from .forms import PartnerForm

class IndexView(TemplateView):
    template_name = 'index.html'

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
        return render(self.request, 'partner_confirm.html', {'form': form})

    def form_finalize(self, form):
        # Save partner instance
        self.object = form.save()

        # Save related instances for product_info and case_study
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

    def form_valid(self, form):
        return self.form_confirm(form)






















