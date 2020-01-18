import json
import random

from django import template
from django.template.loader import render_to_string

from app.models import Song, UserProfile

register = template.Library()


def get_item(dictionary, key):
    if isinstance(dictionary, str):
        dictionary = json.loads(json.loads(dictionary))
    return dictionary.get(key)


def get_dictionnary_items(dictionary):
    return dictionary.items()


def return_song_search_result_template(item):
    songObject = json.loads(item.genius_infos) if isinstance(item, Song) else item
    return render_to_string('song/search-result.html', {
        'object': songObject
    })


def return_playlist_search_result_template(playlist, user):
    return render_to_string('playlist/search-result.html', {
        'object': playlist,
        'user': user
    })


def check_playlist_is_already_followed(playlist, user):
    userProfile = UserProfile.objects.get(user=user)
    playlist = playlist.followers.filter(user_id=userProfile.user.id)
    return True if playlist else False

@register.simple_tag
def random_int(a, b=None):
    if b is None:
        a, b = 0, a
    return random.randint(a, b)


register.filter('get_item', get_item)
register.filter('get_dictionnary_items', get_dictionnary_items)
register.filter('return_song_search_result_template', return_song_search_result_template)
register.filter('return_playlist_search_result_template', return_playlist_search_result_template)
register.filter('check_playlist_is_already_followed', check_playlist_is_already_followed)
