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
from app.views import splash
from app.views.login import UserLoginView, logout_view
from app.views.password_reset import CustomPasswordResetView, password_reset_sent, CustomPasswordResetConfirmView, \
    password_reset_complete
from app.views.register import *
from app.views.search import *

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
