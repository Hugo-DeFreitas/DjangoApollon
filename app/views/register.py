from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView

from app.forms.register import RegisterForm
from app.models import UserProfile


class RegisterView(FormView):
    template_name = 'auth/sign_up.html'
    form_class = RegisterForm
    success_url = '/sign_up/thanks/'

    def form_valid(self, form):
        if form.is_valid():
            newUser = User.objects.create_user(email=form.cleaned_data['email'],
                                               username=form.cleaned_data['username'],
                                               password=form.cleaned_data['password1'],
                                               first_name=form.cleaned_data['first_name'],
                                               last_name=form.cleaned_data['last_name'],
                                               )

            UserProfile.objects.create(user=newUser,
                                       biography=form.cleaned_data['biography'])

        return super().form_valid(form)
