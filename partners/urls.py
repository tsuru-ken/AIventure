from django.urls import path
from . import views

app_name = 'partners'


urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
]

