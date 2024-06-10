from django.urls import path
from .views import AIModelListView, AIModelDetailView, AIModelCreateView, AIModelUpdateView, AIModelDeleteView,AIModelIndexView

app_name = 'ai_models'

urlpatterns = [
    path('', AIModelIndexView.as_view(), name='ai_model_index'),
    path('list/',AIModelListView.as_view(), name='ai_model_list'),
    path('<int:pk>/', AIModelDetailView.as_view(), name='ai_model_detail'),
    path('create/', AIModelCreateView.as_view(), name='ai_model_create'),
    path('<int:pk>/update/', AIModelUpdateView.as_view(), name='ai_model_update'),
    path('<int:pk>/delete/', AIModelDeleteView.as_view(), name='ai_model_delete'),
    
]
