from django.urls import path
from . import views

from users import views as user_views

app_name = 'users'


urlpatterns = [
    
    path ('',user_views.IndexView.as_view(), name = 'index'),
    path('signup/', views.SignUpView.as_view(),name='signup'),
    path('signup_success/', views.SignUpSuccessView.as_view(),name='signup_success'),
    
    
    
]

