from django.shortcuts import render
from django.views.generic import ListView
from .models import AIModel


class AIModelListView(ListView):
    model = AIModel
    template_name = 'ai_model_list.html'
    context_object_name = 'ai_models'
    



