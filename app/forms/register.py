from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import Form, widgets
from django.utils.translation import gettext_lazy as _


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=250,
                               min_length=4,
                               widget=widgets.Input(
                                   attrs={
                                       'class': 'uk-input',
                                       'placeholder': _('Username')
                                   }
                               ))
    email = forms.CharField(max_length=250,
                            min_length=4,
                            widget=widgets.EmailInput(
                                attrs={
                                    'class': 'uk-input',
                                    'placeholder': _('Email')
                                }
                            ))

    first_name = forms.CharField(max_length=250,
                                 label=_('First name'),
                                 widget=widgets.Input(
                                     attrs={
                                         'class': 'uk-input',
                                         'placeholder': _('First name')
                                     }
                                 ))
    last_name = forms.CharField(max_length=250,
                                label=_('Last name'),
                                widget=widgets.Input(
                                    attrs={
                                        'class': 'uk-input',
                                        'placeholder': _('Last name')
                                    }
                                ))

    password1 = forms.CharField(max_length=250,
                                min_length=4,
                                label=_('First password'),
                                widget=widgets.PasswordInput(
                                    attrs={
                                        'class': 'uk-input',
                                        'placeholder': _('Password')
                                    }
                                ))

    password2 = forms.CharField(max_length=250,
                                min_length=4,
                                label=_('Second password'),
                                widget=widgets.PasswordInput(
                                    attrs={
                                        'class': 'uk-input',
                                        'placeholder': _('Repeat password')
                                    }
                                ))

    biography = forms.CharField(max_length=1000,
                                required=False,
                                widget=widgets.Textarea(
                                    attrs={
                                        'class': 'uk-input',
                                        'placeholder': _('Biography')
                                    }
                                ))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
