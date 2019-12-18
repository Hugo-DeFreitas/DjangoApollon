from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import FormView

from app.forms.register import RegisterForm


class RegisterView(FormView):
    template_name = 'auth/sign_up.html'
    form_class = RegisterForm

    def form_valid(self, form):
        User.objects.create_user(email=form.cleaned_data['email'],
                                 username=form.cleaned_data['username'],
                                 password=form.cleaned_data['password_1'])
        super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('app_index')
