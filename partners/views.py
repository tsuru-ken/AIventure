from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from .models import Partners
from .forms import PartnerForm

class IndexView(TemplateView):
    
    template_name = 'index.html'
    
class PartnerCreateView(CreateView):
    model = Partners
    form_class = PartnerForm
    template_name = 'partner_form.html'
    success_url = reverse_lazy('partners:index')
