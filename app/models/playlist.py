from django.db import models

from app.models.song import Song
from app.models.user_profile import UserProfile


class Playlist(models.Model):
    created_by = models.OneToOneField(UserProfile,
                                      on_delete=models.CASCADE,
                                      null=False)
    title = models.CharField(blank=True,
                             null=False,
                             max_length=500)
    description = models.TextField(blank=True,
                                   null=True,
                                   default='No description provided',
                                   max_length=500)
    songs = models.ManyToManyField(Song,
                                   related_name='playlists')
    followers = models.ManyToManyField(UserProfile,
                                       related_name='playlists_followed')

    # Visibilité de la playlist
    is_public = models.BooleanField(blank=True,
                                    null=False,
                                    default=True)

    def __str__(self):
        return '{} ({})'.format(self.title,
                                self.created_by.user.username)
