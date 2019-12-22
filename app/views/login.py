from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from app.forms.login import LoginForm
from app.models import UserProfile


class UserLoginView(LoginView):
    model = UserProfile
    template_name = 'auth/sign_in.html'
    authentication_form = LoginForm

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('app_login'))
