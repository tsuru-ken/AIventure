from django.urls import path
from . import views

app_name = 'image_generation'


urlpatterns = [
    # path('',views.IndexView.as_view(), name='index'),
    
    # 画像生成URL
    path('generate/',views.generate_image, name='generate_image'),
]