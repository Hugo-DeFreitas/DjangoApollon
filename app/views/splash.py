from django.http import HttpResponse
from django.template import loader, context


def splash(request):
    template = loader.get_template('layouts/splash.html')
    return HttpResponse(template.render())