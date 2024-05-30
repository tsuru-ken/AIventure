from django.urls import path
from . import views

app_name = 'aiventure'


urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
]