from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader, context
from django.urls import reverse_lazy

from app.models import UserProfile


def splash(request):
    if not request.user.is_authenticated:
        template = loader.render_to_string('layouts/splash.html')
        return HttpResponse(template)

    currentUser = UserProfile.objects.get(user_id=request.user.id)
    if not currentUser:
        template = loader.render_to_string('layouts/splash.html')
        return HttpResponse(template)
    return HttpResponse(
        loader.render_to_string(
            'layouts/home.html',
            {
                'user_profile': currentUser
            },
            request)
    )
