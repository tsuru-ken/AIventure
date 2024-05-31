from django.urls import path
from .views import AIModelListView

app_name = 'ai_models'

urlpatterns = [
    path('', AIModelListView.as_view(), name= 'ai_model_list'),
]