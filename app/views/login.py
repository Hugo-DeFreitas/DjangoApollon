from django.contrib.auth.views import LoginView

from app.models import UserProfile


class UserLoginView(LoginView):
    model = UserProfile
    template_name = 'auth/sign_in.html'
