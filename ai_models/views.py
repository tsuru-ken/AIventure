from django.views.generic import ListView, DetailView
from .models import AIModel
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import AIModelForm

class AIModelListView(ListView):
    model = AIModel
    template_name = 'ai_model_list.html'
    context_object_name = 'ai_models'
    
class AIModelIndexView(ListView):
    model = AIModel
    template_name = 'ai_model_index.html'
    context_object_name = 'ai_models'
    
class AIModelDetailView(DetailView):
    model = AIModel
    template_name = 'ai_model_detail.html'
    context_object_name = 'ai_model'

class AIModelCreateView(CreateView):
    model = AIModel
    form_class = AIModelForm
    template_name = 'ai_model_form.html'
    success_url = reverse_lazy('ai_models:ai_model_list')

class AIModelUpdateView(UpdateView):
    model = AIModel
    form_class = AIModelForm
    template_name = 'ai_model_form.html'
    success_url = reverse_lazy('ai_models:ai_model_list')

class AIModelDeleteView(DeleteView):
    model = AIModel
    template_name = 'ai_model_confirm_delete.html'
    success_url = reverse_lazy('ai_models:ai_model_list')

    




