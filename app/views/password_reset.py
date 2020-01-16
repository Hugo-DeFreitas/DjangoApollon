from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

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


class PasswordResetWasSentView(TemplateView):
    template_name = 'auth/password_reset_sent.html'


class PasswordResetComplete(TemplateView):
    template_name = 'auth/password_reset_complete.html'
