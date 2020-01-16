from django import forms
from django.forms import widgets
from django.utils.translation import gettext_lazy as _

from app.models import Playlist


class PlaylistForm(forms.ModelForm):
    title = forms.CharField(max_length=250,
                            widget=widgets.Input(
                                attrs={
                                    'class': 'uk-input',
                                    'placeholder': _('Playlist title')
                                }
                            ))
    description = forms.CharField(max_length=400,
                                  widget=widgets.Input(
                                      attrs={
                                          'class': 'uk-input',
                                          'placeholder': _('Playlist description')
                                      }
                                  ))
    picture = forms.CharField(max_length=850,
                              required=False,
                              empty_value='/static/img/album-img-not-found.png',
                              widget=widgets.Input(
                                  attrs={
                                      'class': 'uk-input',
                                      'placeholder': _('Playlist thumbnail'),
                                  }
                              ))

    is_public = forms.BooleanField(label=_('Is public'),
                                   required=False,
                                   widget=widgets.CheckboxInput(
                                       attrs={
                                           'class': 'uk-checkbox',
                                       }
                                   ))

    class Meta:
        model = Playlist
        fields = ('title', 'picture', 'description', 'is_public')
