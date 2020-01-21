import json
from random import randint

import requests
from django.contrib.auth.models import User
from django.db.models import Count
from django.views.generic import TemplateView

from app.models import UserProfile, Playlist, Song
from utils.genius import *


class SplashView(TemplateView):
    def get_template_names(self):
        if not self.request.user.is_authenticated:
            return 'layouts/splash.html'
        return 'layouts/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['playlists_trending'] = (Playlist.objects
                                         .annotate(followers_count=Count('followers'))
                                         .filter(is_public=True)
                                         .order_by('-followers_count'))[:3]
        if self.request.user.is_authenticated:
            context['user_profile'] = UserProfile.objects.get(user=self.request.user)

            # On vient extraire des suggestions pour la page d'accueil
            randomSong = Song.objects.all()[randint(0, Song.objects.all().count() - 1)]
            randomSongInfos = json.loads(randomSong.genius_infos)
            payload = {
                'genius_client_id': GENIUS_API_CLIENT_ID,
                'genius_secret_id': GENIUS_API_CLIENT_SECRET,
            }
            randomGeniusArtist = json.loads(
                requests.get(getArtistEndpoint(randomSongInfos.get('primary_artist').get('id')),
                             params=payload).text).get('response').get('artist')
            context['new_users'] = UserProfile.objects.filter(user__in=User.objects.all().order_by('-date_joined')[:5])
            context['random_artist'] = randomGeniusArtist
        return context
