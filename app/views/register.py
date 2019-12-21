from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse, reverse_lazy

from DjangoApollon.settings import *
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView

from app.forms.register import RegisterForm
from app.models import UserProfile


class RegisterView(FormView):
    template_name = 'auth/sign_up.html'
    form_class = RegisterForm
    success_url = '/sign_up/thanks'

    def form_valid(self, form):
        if form.is_valid():
            newUser = User.objects.create_user(email=form.cleaned_data['email'],
                                               username=form.cleaned_data['username'],
                                               password=form.cleaned_data['password1'],
                                               first_name=form.cleaned_data['first_name'],
                                               last_name=form.cleaned_data['last_name'],
                                               )

            newUserProfile = UserProfile.objects.create(user=newUser,
                                                        biography=form.cleaned_data['biography'])

            # On envoie un mail de confirmation du compte.
            redirectAccountConfirmationURL = Site.objects.get_current().domain + reverse('app_account_confirmation',
                                                                                         args=[
                                                                                             newUserProfile.confirmation_token])
            send_mail(
                _('Thanks for signing up'),
                _('Signing up message'),
                APOLLON_MAIL,
                [newUser.email],
                fail_silently=False,
                html_message=loader.render_to_string('mail/welcome.html', {
                    'username': newUser.username,
                    'confirmation_url': redirectAccountConfirmationURL
                })
            )

        return super().form_valid(form)


def thanks_for_signing_up(request):
    if request.user.is_authenticated:
        if UserProfile.objects.get(pk=request.user.id).is_valid:
            return HttpResponseNotFound('You have already received our congratulations')
        template = loader.get_template('auth/thanks.html')
        return HttpResponse(template.render())
    else:
        return HttpResponseNotFound()


def account_confirmation(request, token):
    if request.user.is_authenticated:
        return HttpResponse(UserProfile.objects.get(confirmation_token=token).user.username)
    else:
        redirect(reverse_lazy('app_login'))
