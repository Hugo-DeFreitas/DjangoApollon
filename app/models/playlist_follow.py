from django.db import models

from app.models.playlist import Playlist
from app.models.user_profile import UserProfile


class PlaylistFollow(models.Model):
    user = models.OneToOneField(UserProfile,
                                on_delete=models.CASCADE,
                                null=False)
    playlist = models.OneToOneField(Playlist,
                                    on_delete=models.CASCADE,
                                    null=False)

    def __str__(self):
        return '{} -> {} : {}'.format(self.user.username,
                                      self.playlist.created_by.user.username,
                                      self.playlist)
