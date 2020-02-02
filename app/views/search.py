import json

import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView
from difflib import get_close_matches

from app.models import UserProfile, Playlist
from utils.genius import *


def searchSongs(request, search):
    payload = {
        'genius_client_id': GENIUS_API_CLIENT_ID,
        'genius_secret_id': GENIUS_API_CLIENT_SECRET,
    }
    response = requests.get(getSearchEndpoint(search),
                            params=payload)
    return JsonResponse(response.text, safe=False)


def getSong(request, search):
    payload = {
        'genius_client_id': GENIUS_API_CLIENT_ID,
        'genius_secret_id': GENIUS_API_CLIENT_SECRET,
    }
    response = requests.get(getSongEndpoint(search),
                            params=payload)
    return JsonResponse(response.text, safe=False)


def getArtist(request, search):
    payload = {
        'genius_client_id': GENIUS_API_CLIENT_ID,
        'genius_secret_id': GENIUS_API_CLIENT_SECRET,
    }
    response = requests.get(getArtistEndpoint(search),
                            params=payload)
    return JsonResponse(response.text, safe=False)


class SongSearchEngine(LoginRequiredMixin, TemplateView):
    template_name = 'song/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        payload = {
            'genius_client_id': GENIUS_API_CLIENT_ID,
            'genius_secret_id': GENIUS_API_CLIENT_SECRET,
        }
        response = None
        if self.request.GET.get('search'):
            response = requests.get(getSearchEndpoint(self.request.GET.get('search')),
                                    params=payload)
            response = json.loads(response.text).get('response').get('hits') if response is not None else None
        context['api_response'] = response
        context['user_playlists'] = Playlist.objects.filter(created_by=UserProfile.objects.get(user=self.request.user))
        return context


class PlaylistSearchEngine(LoginRequiredMixin, ListView):
    template_name = 'playlist/search.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # By default, the suggestions contains the 5 most recent playlists created
        context['suggestions'] = Playlist.objects.order_by('-created_at')[:5]
        # If there are no playlists found with the user query, let's give him name-based playlists choices
        if not self.object_list and self.request.GET.get('search'):
            allSimilarPlaylists = Playlist.objects.filter(
                title__in=get_close_matches(word=self.request.GET.get('search'),
                                            possibilities=[title.get('title') for title in
                                                           Playlist.objects.filter(is_public=True).values('title')],
                                            cutoff=0.2))
            context['suggestions'] = allSimilarPlaylists[:5]
        return context

    def get_queryset(self):
        return Playlist.objects.filter(
            title__icontains=self.request.GET.get('search') if self.request.GET.get('search') is not None else '',
            is_public=True) \
                   .exclude(created_by__user=self.request.user)[:10]
