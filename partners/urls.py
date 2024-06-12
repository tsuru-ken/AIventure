from django.urls import path
from . import views

app_name = 'partners'

urlpatterns = [
    path('', views.PartnerListView.as_view(), name='index'),
    path('create/', views.PartnerCreateView.as_view(), name='partner_create'),
    path('<int:pk>/',views.PartnerDetailView.as_view(), name='partner_detail'),
]





