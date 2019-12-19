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
from app.views.login import UserLoginView
from app.views.search import searchSongs, getSong

urlpatterns = [
    url('^$', splash, name='app_home'),
    path('admin/', admin.site.urls),
    url(r'^sign_in/?$', UserLoginView.as_view(), name='app_login'),
    url(r'^sign_up/?$', RegisterView.as_view(), name='app_register'),
    path('search/<str:search>', searchSongs, name='search_songs'),
    path('search/song/<int:search>', getSong, name='get_song'),
]

urlpatterns += i18n_patterns(
    url(r'^sign_in/?$', LoginView.as_view(), name='app_login'),
    path('home/', splash, name='app_home'),
)
