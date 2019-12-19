from django.contrib.sites.models import Site
from django.db import models
from django.urls import reverse


class Song(models.Model):
    genius_id = models.IntegerField(blank=True)

    def getGeniusInfos(self):
        return Site.objects.get_current().domain + reverse('get_song',
                                                           args=[self.genius_id])
