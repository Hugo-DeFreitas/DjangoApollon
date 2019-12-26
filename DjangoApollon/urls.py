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
from app.views import *
from app.views.playlist import PlaylistList, PlaylistDetail

urlpatterns = [
    # Page d'accueil
    url('^$', splash, name='app_home'),
    # Admin
    path('admin/', admin.site.urls),
    # Authentification
    url(r'^sign_in/?$', UserLoginView.as_view(), name='app_login'),
    url(r'^sign_up/?$', RegisterView.as_view(), name='app_register'),
    url(r'^sign_out/?$', logout_view, name='app_logout'),
    path('reset_password/', CustomPasswordResetView.as_view(), name='app_reset_password'),
    path('reset_password/sent', password_reset_sent, name='app_reset_password_mail_sent'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', CustomPasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    path('reset_password/complete', password_reset_complete, name='password_reset_complete'),
    path('sign_up/thanks', thanks_for_signing_up, name='app_thanks_for_signing_up'),
    path('sign_up/account_confirmation', account_confirmation, name='app_account_confirmation'),
    # Moteur de recherche
    path('search/<str:search>', searchSongs, name='search_songs'),
    path('search/song/<int:search>', getSong, name='get_song'),
    path('search/artist/<int:search>', getSong, name='get_artist'),
    # Changement de langue
    path('change_lang/<str:lang_code>', change_language, name='app_change_language'),
    # Core Apollon
    path('me/playlists/new', splash, name='app_new_playlist'),
    path('me/playlists', PlaylistList.as_view(), name='app_user_playlists'),
    path('playlists/<str:username>/<slug:pk>', PlaylistDetail.as_view(), name='app_playlist_detail'),
    path('playlists/delete', PlaylistDetail.as_view(), name='app_playlist_delete'),
    path('playlists/unfollow', PlaylistDetail.as_view(), name='app_playlist_unfollow'),
    path('search/playlists', splash, name='app_search_playlists'),
    path('search/songs', splash, name='app_search_songs'),

]

urlpatterns += i18n_patterns(
    # Page d'accueil
    url('^$', splash, name='app_home'),
    # Authentification
    url(r'^sign_in/?$', UserLoginView.as_view(), name='app_login'),
    url(r'^sign_up/?$', RegisterView.as_view(), name='app_register'),
    url(r'^sign_out/?$', logout_view, name='app_logout'),
    path('reset_password/', CustomPasswordResetView.as_view(), name='app_reset_password'),
    path('reset_password/sent', password_reset_sent, name='app_reset_password_mail_sent'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', CustomPasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    path('reset_password/complete', password_reset_complete, name='password_reset_complete'),
    path('sign_up/thanks', thanks_for_signing_up, name='app_thanks_for_signing_up'),
    path('sign_up/account_confirmation', account_confirmation, name='app_account_confirmation'),
)
