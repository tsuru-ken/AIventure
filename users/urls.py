from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('', user_views.IndexView.as_view(), name='index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup_success/', views.SignUpSuccessView.as_view(), name='signup_success'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('guest_login/<str:user_type>/', views.guest_login, name='guest_login'),
    path('admin_view/', views.admin_view, name='admin_view'),
]
