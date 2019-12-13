from django.db import models

from app.models.user_profile import UserProfile


class Playlist(models.Model):
    created_by = models.OneToOneField(UserProfile,
                                      on_delete=models.CASCADE,
                                      null=False)
    description = models.TextField(blank=True,
                                   null=True,
                                   default='No description provided',
                                   max_length=500)
    # Visibilité de la playlist
    is_public = models.BooleanField(blank=True,
                                    null=False,
                                    default=True)

    def __str__(self):
        return '{} ({} {})'.format(self.user.username,
                                   self.user.first_name,
                                   self.user.last_name)
