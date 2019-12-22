from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
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
    success_url = reverse_lazy('app_thanks_for_signing_up')

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
            user = authenticate(self.request, username=newUser.username, password=form.cleaned_data['password1'])
            if user is not None:
                login(self.request, user)

            # On envoie un mail de confirmation du compte.
            redirectAccountConfirmationURL = Site.objects.get_current().domain + reverse('app_account_confirmation') \
                                             + '?token=' \
                                             + newUserProfile.confirmation_token
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

@login_required
def thanks_for_signing_up(request):
    if request.user.is_authenticated:
        if UserProfile.objects.get(user_id=request.user.id).is_valid:
            return redirect(reverse_lazy('app_home'))
        template = loader.get_template('auth/thanks.html')
        return HttpResponse(template.render())
    else:
        return HttpResponseNotFound()


@login_required
def account_confirmation(request):
    token = request.GET.get('token')
    if token:
        user_profile = UserProfile.objects.get(confirmation_token=token)
        if user_profile and not user_profile.is_valid:
            user_profile.is_valid = True
            user_profile.save()
            # La validation est passée
            send_mail(
                _('Thanks for signing up'),
                _('Signing up message'),
                APOLLON_MAIL,
                [user_profile.user.email],
                fail_silently=False,
                html_message=loader.render_to_string('mail/account_validated.html', {
                    'username': user_profile.user.username,
                })
            )
            return HttpResponse(loader.render_to_string('auth/account_validated.html',
                                                        {
                                                            'user_profile': user_profile
                                                        }))
        elif user_profile and user_profile.is_valid:
            return redirect(reverse_lazy('app_home'))
        else:
            return HttpResponseNotFound()

    else:
        return HttpResponseNotFound()
