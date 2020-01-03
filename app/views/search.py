import json

from django.http import HttpResponse
from django.template import loader

from utils.genius import *
import requests


def searchSongs(request, search):
    payload = {
        'genius_client_id': GENIUS_API_CLIENT_ID,
        'genius_secret_id': GENIUS_API_CLIENT_SECRET,
    }
    response = requests.get(getSearchEndpoint(search),
                            params=payload)
    return HttpResponse(response)


def getSong(request, search):
    payload = {
        'genius_client_id': GENIUS_API_CLIENT_ID,
        'genius_secret_id': GENIUS_API_CLIENT_SECRET,
    }
    response = requests.get(getSongEndpoint(search),
                            params=payload)
    return HttpResponse(response)


def getArtist(request, search):
    payload = {
        'genius_client_id': GENIUS_API_CLIENT_ID,
        'genius_secret_id': GENIUS_API_CLIENT_SECRET,
    }
    response = requests.get(getArtistEndpoint(search),
                            params=payload)
    return HttpResponse(response)


def songsSearchEngineView(request):
    payload = {
        'genius_client_id': GENIUS_API_CLIENT_ID,
        'genius_secret_id': GENIUS_API_CLIENT_SECRET,
    }
    response = None
    if request.GET.get('search'):
        response = requests.get(getSearchEndpoint(request.GET.get('search')),
                                params=payload)
        response = json.loads(response.text).get('response').get('hits') if response is not None else None
    template = loader.render_to_string('song/search.html', {
        'request': request,
        'api_response': response
    })
    return HttpResponse(template)
