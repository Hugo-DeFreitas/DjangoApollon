from django.template.defaulttags import register
from django.template.loader import render_to_string


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_dictionnary_items(dictionary):
    return dictionary.items()


@register.filter
def return_search_result_template(item):
    return render_to_string('song/search-result.html', {
        'object': item.get('result')
    })
