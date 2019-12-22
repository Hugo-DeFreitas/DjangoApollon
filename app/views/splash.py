from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader, context
from django.urls import reverse_lazy

from app.models import UserProfile


def splash(request):
    if request.user.is_authenticated:
        return HttpResponse(
            loader.render_to_string(
                'layouts/home.html',
                {
                    'user_profile': UserProfile.objects.get(user_id=request.user.id)
                },
                request)
        )
    else:
        template = loader.render_to_string('layouts/splash.html')
        return HttpResponse(template)
