from django.db import models


class Track(models.Model):
    mbid = models.TextField(blank=True,
                            unique=True,
                            null=False,
                            max_length=150)
