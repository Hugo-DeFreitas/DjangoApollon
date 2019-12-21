from django.contrib.auth.models import User
from django.db import models
from django.utils.crypto import get_random_string


class UserProfile(models.Model):
    """
    Profile d'un utilisateur. On utilise une relation One To One vers le modèle Django basique "User".
    Ce modèle contient donc toutes les infos supplémentaires des utilisateurs (bio, validation de mail, etc.).
    """
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                null=False)
    biography = models.TextField(blank=True,
                                 null=True,
                                 default='No description provided',
                                 max_length=300)
    # Validation mail de l'utilisateur
    is_valid = models.BooleanField(blank=True,
                                   null=True,
                                   default=False)
    confirmation_token = models.CharField(blank=True,
                                          null=True,
                                          default=get_random_string(length=32),
                                          max_length=32)

    def __str__(self):
        return '{} ({} {})'.format(self.user.username,
                                   self.user.first_name,
                                   self.user.last_name)
