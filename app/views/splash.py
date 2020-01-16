from django.db.models import Count
from django.http import HttpResponse
from django.template import loader

from app.models import UserProfile, Playlist


def splash(request):
    if not request.user.is_authenticated:
        template = loader.render_to_string('layouts/splash.html')
        return HttpResponse(template)

    currentUser = UserProfile.objects.get(user_id=request.user.id)
    if not currentUser:
        template = loader.render_to_string('layouts/splash.html')
        return HttpResponse(template)
    mostFollowedPlaylists = (Playlist.objects
                             .annotate(followers_count=Count('followers'))
                             .order_by('-followers_count'))[:5]
    return HttpResponse(
        loader.render_to_string(
            'layouts/home.html',
            {
                'user_profile': currentUser,
                'playlists_trending': mostFollowedPlaylists
            },
            request)
    )