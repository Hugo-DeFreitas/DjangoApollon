from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse_lazy

from app.forms.password_reset import CustomPasswordResetForm, CustomPasswordResetConfirmForm


class CustomPasswordResetView(PasswordResetView):
    template_name = 'auth/password_reset_ask.html'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('app_reset_password_mail_sent')
    html_email_template_name = 'mail/reset_password.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'auth/password_reset_confirm.html'
    form_class = CustomPasswordResetConfirmForm
    success_url = reverse_lazy('password_reset_complete')


def password_reset_sent(request):
    return HttpResponse(loader.render_to_string('auth/password_reset_sent.html'))

def password_reset_complete(request):
    return HttpResponse(loader.render_to_string('auth/password_reset_complete.html'))
