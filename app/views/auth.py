from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from app.forms.login import LoginForm


class UserLoginView(LoginView):
    template_name = 'auth/sign_in.html'
    authentication_form = LoginForm


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('app_home')
