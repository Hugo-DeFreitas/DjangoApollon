"""DjangoApollon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path
from django.views import static

from app.views import *
from app.views.playlist import PlaylistList, PlaylistDetail, PlaylistCreate, PlaylistDelete, PlaylistUpdate, \
    follow_playlist, unfollow_playlist, delete_song_from_playlist
from app.views.profile import ProfileUpdate, PublicProfile
from app.views.song import SongDetail, create_if_not_exists, add_song_to_playlist

urlpatterns = [
    # Favicon
    url(r'^favicon.ico/$', lambda x: HttpResponseRedirect(settings.STATIC_URL + 'favicon.ico')),

    # Page d'accueil
    url('^$', SplashView.as_view(), name='app_home'),
    # Admin
    path('admin/', admin.site.urls),
    # Authentification
    url(r'^sign_in/?$', UserLoginView.as_view(), name='app_login'),
    url(r'^sign_out/?$', UserLogoutView.as_view(), name='app_logout'),
    url(r'^sign_up/?$', RegisterView.as_view(), name='app_register'),
    path('reset_password/', CustomPasswordResetView.as_view(), name='app_reset_password'),
    path('reset_password/sent', PasswordResetWasSentView.as_view(), name='app_reset_password_mail_sent'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', CustomPasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    path('reset_password/complete', PasswordResetComplete.as_view(), name='password_reset_complete'),
    path('sign_up/thanks', ThanksForSigningUpView.as_view(), name='app_thanks_for_signing_up'),
    path('sign_up/account_confirmation', AccountConfirmationView.as_view(), name='app_account_confirmation'),
    # Moteur de recherche
    path('search_engine/<str:search>', searchSongs, name='search_songs'),
    path('search_engine/song/<int:search>', getSong, name='get_song'),
    path('search_engine/artist/<int:search>', getSong, name='get_artist'),
    # Changement de langue
    path('change_lang/<str:lang_code>', change_language, name='app_change_language'),

    # Gestion du profil
    path('me/update/<int:pk>', ProfileUpdate.as_view(), name='app_profile_update'),
    # Profils publics
    url(r'^profiles/(?P<slug>[\w.@+-]+)$', PublicProfile.as_view(), name='app_public_profile'),

    # Core Apollon
    # Gestion des playlists (création, liste personnelle, etc.)
    path('me/playlists/new', PlaylistCreate.as_view(), name='app_new_playlist'),
    path('me/playlists', PlaylistList.as_view(), name='app_user_playlists'),
    path('me/playlists/delete/<int:pk>', PlaylistDelete.as_view(), name='app_playlist_delete'),
    path('me/playlists/update/<int:pk>', PlaylistUpdate.as_view(), name='app_playlist_update'),
    path('playlists/<str:username>/<slug:pk>', PlaylistDetail.as_view(), name='app_playlist_detail'),
    path('playlists/follow', follow_playlist, name='follow_playlist'),
    path('playlists/unfollow', unfollow_playlist, name='unfollow_playlist'),
    path('playlists/delete-song-from-playlist', delete_song_from_playlist, name='delete_song_from_playlist'),

    # Gestion des chansons (détail, recherche et ajout à une playlist existante).
    path('me/add-song-to-playlist/', add_song_to_playlist, name='app_add_song_to_playlist'),
    path('song/<slug:slug>', SongDetail.as_view(), name="app_song_detail"),
    path('song/create_if_not_exists/<int:genius_id>', create_if_not_exists, name="app_create_song_if_not_exists"),

    # Vue des moteurs de recherche
    path('search/playlists', PlaylistSearchEngine.as_view(), name='app_search_playlists'),
    path('search/songs', SongSearchEngine.as_view(), name='app_search_songs'),
]

urlpatterns += i18n_patterns(
    # Page d'accueil
    url('^$', SplashView.as_view(), name='app_home'),
    url(r'^sign_in/?$', UserLoginView.as_view(), name='app_login'),
    url(r'^sign_out/?$', UserLogoutView.as_view(), name='app_logout'),
    url(r'^sign_up/?$', RegisterView.as_view(), name='app_register'),
    path('reset_password/', CustomPasswordResetView.as_view(), name='app_reset_password'),
    path('reset_password/sent', PasswordResetWasSentView.as_view(), name='app_reset_password_mail_sent'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', CustomPasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    path('reset_password/complete', PasswordResetComplete.as_view(), name='password_reset_complete'),
    path('sign_up/thanks', ThanksForSigningUpView.as_view(), name='app_thanks_for_signing_up'),
    path('sign_up/account_confirmation', AccountConfirmationView.as_view(), name='app_account_confirmation'),

    # Gestion du profil
    path('me/update/<int:pk>', ProfileUpdate.as_view(), name='app_profile_update'),
    # Profils publics
    url(r'^profiles/(?P<slug>[\w.@+-]+)$', PublicProfile.as_view(), name='app_public_profile'),

    # Core Apollon
    # Gestion des playlists (création, liste personnelle, etc.)
    path('me/playlists/new', PlaylistCreate.as_view(), name='app_new_playlist'),
    path('me/playlists', PlaylistList.as_view(), name='app_user_playlists'),
    path('me/playlists/delete/<int:pk>', PlaylistDelete.as_view(), name='app_playlist_delete'),
    path('me/playlists/update/<int:pk>', PlaylistUpdate.as_view(), name='app_playlist_update'),
    path('playlists/<str:username>/<slug:pk>', PlaylistDetail.as_view(), name='app_playlist_detail'),
    # Gestion des chansons (détail, recherche et ajout à une playlist existante).
    path('song/<slug:slug>', SongDetail.as_view(), name="app_song_detail"),
    # Vue des moteurs de recherche
    path('search/playlists', PlaylistSearchEngine.as_view(), name='app_search_playlists'),
    path('search/songs', SongSearchEngine.as_view(), name='app_search_songs'),
)
