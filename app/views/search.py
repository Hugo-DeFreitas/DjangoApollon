from django.http import HttpResponse

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
    pass