from django.db import models


class Song(models.Model):
    genius_id = models.IntegerField(blank=True)
