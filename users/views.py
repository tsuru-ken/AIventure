from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('users:signup_success')

    def form_valid(self, form):
        user = form.save()
        self.get_object = user
        return super().form_valid(form)

class SignUpSuccessView(TemplateView):
    template_name = 'signup_success.html'

class IndexView(TemplateView):
    template_name = 'index.html'

def guest_login(request, user_type):
    if user_type == 'admin':
        user = authenticate(username='admin_guest', password='guestpassword')
    else:
        user = authenticate(username='guest', password='guestpassword')
    if user is not None:
        login(request, user)
        return redirect('users:index')
    return redirect('users:login')

def admin_required(view_func):
    decorated_view_func = user_passes_test(lambda u: u.is_superuser, login_url='users:login')(view_func)
    return decorated_view_func

@admin_required
def admin_view(request):
    return redirect('/admin/')

