from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils import translation


def change_language(request, lang_code):
    """
    Permet à l'utilisateur de changer le language du site
    """
    translation.activate(lang_code)
    response = HttpResponseRedirect(reverse_lazy('app_home'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    return response
