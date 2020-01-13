import json

from django.template.defaulttags import register
from django.template.loader import render_to_string

from app.models import Song


@register.filter
def get_item(dictionary, key):
    if isinstance(dictionary, str):
        dictionary = json.loads(json.loads(dictionary))
    return dictionary.get(key)


@register.filter
def get_dictionnary_items(dictionary):
    return dictionary.items()


@register.filter
def return_search_result_template(item):
    songObject = json.loads(item.genius_infos) if isinstance(item, Song) else item
    return render_to_string('song/search-result.html', {
        'object': songObject
    })
