from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import widgets

from django.utils.translation import gettext_lazy as _


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=250,
                               min_length=4,
                               widget=widgets.Input(
                                   attrs={
                                       'class': 'uk-input',
                                       'placeholder': _('Username')
                                   }
                               ))

    password = forms.CharField(max_length=250,
                               min_length=4,
                               label=_('Password'),
                               widget=widgets.PasswordInput(
                                   attrs={
                                       'class': 'uk-input',
                                       'placeholder': _('Password')
                                   }
                               ))
