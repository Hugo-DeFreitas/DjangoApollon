import requests
from django.contrib.sites.models import Site
from django.db import models
from django.urls import reverse

from django.core.serializers.json import DjangoJSONEncoder
import json

from django.utils.text import slugify


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
    title = models.CharField(blank=True,
                             null=True,
                             default='Untitled',
                             max_length=100)
    genius_artist_id = models.IntegerField(blank=True,
                                           null=True,
                                           default=None)
    genius_infos = JSONField(blank=True,
                             null=True)
    slug = models.SlugField(null=True,
                            blank=True,
                            unique=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.title)
        super().save(force_insert, force_update, using, update_fields)

    def getGeniusInfosFromAPI(self, update_self=False):
        apiData = json.loads(requests
                             .get(Site.objects.get_current().domain + reverse('get_song', args=[self.genius_id]))
                             .content)
        if update_self:
            self.genius_infos = apiData
            self.save()
        return apiData

    def getArtistGeniusInfosFromAPI(self):
        return json.loads(requests.get(
            Site.objects.get_current().domain + reverse('get_artist', args=[self.genius_artist_id])).content)

    def get_absolute_url(self):
        return reverse('app_song_detail', kwargs={'slug': self.slug})
