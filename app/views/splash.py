from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader, context
from django.urls import reverse_lazy


def splash(request):
    if request.user.is_authenticated:
        template = loader.get_template('layouts/splash.html')
        return HttpResponse(template.render())
    else:
        return redirect(reverse_lazy('app_login'))
