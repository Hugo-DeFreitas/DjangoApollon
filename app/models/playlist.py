from django.db import models

from app.models.song import Song
from app.models.user_profile import UserProfile


class Playlist(models.Model):
    created_by = models.ForeignKey(UserProfile,
                                   blank=True,
                                   null=True,
                                   unique=False,
                                   on_delete=models.CASCADE)
    title = models.CharField(blank=True,
                             null=False,
                             max_length=500)
    picture = models.TextField(blank=True,
                               null=True,
                               default='/static/img/album-img-not-found.png',
                               max_length=500)
    description = models.TextField(blank=True,
                                   null=True,
                                   default='No description provided',
                                   max_length=500)
    songs = models.ManyToManyField(Song,
                                   blank=True,
                                   related_name='playlists')
    followers = models.ManyToManyField(UserProfile,
                                       blank=True,
                                       related_name='playlists_followed')
    created_at = models.DateTimeField(blank=True,
                                      null=True,
                                      auto_now_add=True)

    # Visibilité de la playlist
    is_public = models.BooleanField(blank=True,
                                    null=False,
                                    default=True)

    def __str__(self):
        return '{} (by {})'.format(self.title,
                                   self.created_by.user.username)
