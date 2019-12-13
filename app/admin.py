from django.contrib import admin

from app.models import *

admin.site.register(Playlist)
admin.site.register(PlaylistFollow)
admin.site.register(Track)
admin.site.register(UserProfile)
