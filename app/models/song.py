import collections

import requests
from django.contrib.sites.models import Site
from django.db import models
from django.db.models import TextField
from django.urls import reverse

import json

from django.utils.text import slugify

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
    genius_infos = TextField(blank=True,
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
            self.genius_infos = json.dumps(apiData)
            self.save()
        return apiData

    def getArtistGeniusInfosFromAPI(self):
        return json.loads(requests.get(
            Site.objects.get_current().domain + reverse('get_artist', args=[self.genius_artist_id])).content)

    def get_absolute_url(self):
        return reverse('app_song_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return '{} -> {}'.format(self.genius_id, self.title)
