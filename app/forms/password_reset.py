from django import forms
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm, SetPasswordForm
from django.forms import widgets
from django.utils.translation import gettext_lazy as _


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.CharField(max_length=250,
                            min_length=4,
                            widget=widgets.EmailInput(
                                attrs={
                                    'class': 'uk-input',
                                    'placeholder': _('Email')
                                }
                            ))


class CustomPasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(max_length=250,
                                    min_length=4,
                                    label=_('First password'),
                                    widget=widgets.PasswordInput(
                                        attrs={
                                            'class': 'uk-input',
                                            'placeholder': _('Password')
                                        }
                                    ))

    new_password2 = forms.CharField(max_length=250,
                                    min_length=4,
                                    label=_('Second password'),
                                    widget=widgets.PasswordInput(
                                        attrs={
                                            'class': 'uk-input',
                                            'placeholder': _('Repeat password')
                                        }
                                    ))
