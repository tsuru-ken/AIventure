from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import  CreateView,TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


class SignUpView(CreateView):
    
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    
    success_url = reverse_lazy('users:signup_success')
    def form_valid(self, form):
        
        user = form.save()
        self.get_object = user
        return super().form_valid(form)


class SignUpSuccessView(TemplateView):
    
    template_name = 'signup_success.html'
    

class IndexView(TemplateView):
    template_name = 'index.html'

