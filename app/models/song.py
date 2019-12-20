import requests
from django.contrib.sites.models import Site
from django.db import models
from django.urls import reverse

from django.core.serializers.json import DjangoJSONEncoder
import json


class JSONField(models.TextField):
    """
    Le JSONField n'existe pas pour les BDD SQLLite. Donc en voici un fait maison.
    """

    def to_python(self, value):
        if value == "":
            return None

        try:
            if isinstance(value, str):
                return json.loads(value)
        except ValueError:
            pass
        return value

    def from_db_value(self, value, *args):
        return self.to_python(value)

    def get_db_prep_save(self, value, *args, **kwargs):
        if value == "":
            return None
        if isinstance(value, dict):
            value = json.dumps(value, cls=DjangoJSONEncoder)
        return value


class Song(models.Model):
    genius_id = models.IntegerField(blank=True,
                                    null=True,
                                    default=None)
    genius_artist_id = models.IntegerField(blank=True,
                                           null=True,
                                           default=None)
    genius_infos = JSONField(blank=True,
                             null=True)

    def getGeniusInfosFromAPI(self):
        return json.loads(requests.get(Site.objects.get_current().domain + reverse('get_song', args=[self.genius_id])).content)

    def getArtistGeniusInfosFromAPI(self):
        return json.loads(requests.get(Site.objects.get_current().domain + reverse('get_artist', args=[self.genius_artist_id])).content)
