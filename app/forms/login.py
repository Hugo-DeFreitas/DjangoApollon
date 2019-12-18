from django.forms import models

from app.models import UserProfile


class LoginForm(models.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password']
