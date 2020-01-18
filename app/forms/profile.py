from django import forms
from django.contrib.auth.models import User
from django.forms import widgets, ModelForm
from django.utils.translation import gettext_lazy as _


class ProfileForm(ModelForm):
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

    biography = forms.CharField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name')