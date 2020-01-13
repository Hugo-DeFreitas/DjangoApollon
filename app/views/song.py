import json

import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.views.generic import DetailView

from app.models import Song, Playlist
from utils.genius import *


class SongDetail(LoginRequiredMixin, DetailView):
    template_name = 'song/detail.html'
    model = Song

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        songData = json.loads(self.object.genius_infos)
        context['song'] = songData
        return context


def create_if_not_exists_wrapper(request, genius_id):
    song = Song.objects.filter(genius_id=genius_id).first()
    # Si le son n'existe pas, on va venir l'enregistrer dans la base de données (comme ça on aspire toute l'API de
    # Genius au passage ;)
    if song is not None:
        return song
    payload = {
        'genius_client_id': GENIUS_API_CLIENT_ID,
        'genius_secret_id': GENIUS_API_CLIENT_SECRET,
    }
    songFromAPI = json.loads(requests.get(getSongEndpoint(genius_id),
                                          params=payload).text).get('response').get('song')
    song = Song(title=songFromAPI.get('title'),
                genius_id=genius_id,
                genius_infos=json.dumps(songFromAPI))
    song.save()
    return song


def create_if_not_exists(request, genius_id):
    song = create_if_not_exists_wrapper(request, genius_id)
    return redirect('app_song_detail', slug=song.slug)


def add_song_to_playlist(request):
    genius_id = request.POST.get('genius_id')
    playlist_id = request.POST.get('playlist_id')
    song = create_if_not_exists_wrapper(request, genius_id)
    playlist = Playlist.objects.filter(pk=playlist_id).get()
    playlist.songs.add(song)
    playlist.save()
    return JsonResponse(serializers.serialize('json', [playlist, ]), safe=False)
