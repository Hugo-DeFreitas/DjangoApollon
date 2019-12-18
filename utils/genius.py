import urllib.parse

from DjangoApollon.settings import *

def getSearchEndpoint(search):
    return GENIUS_API_MAIN_ENDPOINT + 'search?q='+urllib.parse.quote(search) + '&access_token=' +\
           GENIUS_API_CLIENT_TOKEN

def getSongEndpoint(song_id):
    return GENIUS_API_MAIN_ENDPOINT + 'songs/' + song_id + '&access_token=' + \
           GENIUS_API_CLIENT_TOKEN
