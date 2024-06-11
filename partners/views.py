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

    def form_valid(self, form):
        request = self.request
        product_info_name = request.POST.get('product_info_name')
        product_info_content = request.POST.get('product_info_content')
        product_info_image = request.FILES.get('product_info_image')
        
        case_study_name = request.POST.get('case_study_name')
        case_study_content = request.POST.get('case_study_content')
        case_study_image = request.FILES.get('case_study_image')
        
        if 'finalize' in request.POST:
            response = super().form_valid(form)
            form.instance.service_content.set(form.cleaned_data['service_content'])
            form.instance.ai_category.set(form.cleaned_data['ai_category'])
            form.instance.cost.set(form.cleaned_data['cost'])
            form.instance.product_info.set(form.cleaned_data['product_info'])
            form.instance.case_study.set(form.cleaned_data['case_study'])

            product_info = ProductInfo(
                partner=form.instance,
                name=product_info_name,
                content=product_info_content,
                image=product_info_image
            )
            product_info.save()

            case_study = CaseStudy(
                partner=form.instance,
                name=case_study_name,
                content=case_study_content,
                image=case_study_image
            )
            case_study.save()

            return response
        elif 'confirm' in request.POST:
            return render(request, 'partner_confirm.html', {'form': form})
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            if 'confirm' in request.POST:
                return render(request, 'partner_confirm.html', {'form': form})
            return self.form_valid(form)
        else:
            return self.form_invalid(form)



















