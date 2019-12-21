from django.contrib.auth.views import LoginView
from django.urls import reverse

from app.forms.login import LoginForm
from app.models import UserProfile


class UserLoginView(LoginView):
    model = UserProfile
    template_name = 'auth/sign_in.html'
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse('app_home')
