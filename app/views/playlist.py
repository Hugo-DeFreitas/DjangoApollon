from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, FormView, CreateView, DeleteView, UpdateView

from app.forms.playlist import PlaylistForm
from app.models import Playlist, UserProfile


class PlaylistList(LoginRequiredMixin, ListView):
    template_name = 'playlist/list.html'
    model = Playlist

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['playlists_followed'] = Playlist.objects.filter(followers__user=self.request.user)
        mostFollowedPlaylists = (Playlist.objects
                                 .annotate(followers_count=Count('followers'))
                                 .order_by('-followers_count'))[:5]
        context['playlists_trending'] = mostFollowedPlaylists
        return context

    def get_queryset(self):
        return Playlist.objects.filter(created_by__user_id=self.request.user.id)


class PlaylistDetail(LoginRequiredMixin, DetailView):
    template_name = 'playlist/detail.html'
    model = Playlist
    slug_url_kwarg = 'not_slug'


class PlaylistCreate(LoginRequiredMixin, CreateView):
    model = Playlist
    template_name = 'playlist/create.html'
    success_url = reverse_lazy('app_home')
    form_class = PlaylistForm

    def form_valid(self, form):
        if not form.is_valid():
            return False
        self.object = form.save()
        self.object.created_by = UserProfile.objects.get(user=self.request.user)
        return super().form_valid(form)


class PlaylistUpdate(LoginRequiredMixin, UpdateView):
    model = Playlist
    template_name = 'playlist/update.html'
    success_url = reverse_lazy('app_home')
    form_class = PlaylistForm


class PlaylistDelete(LoginRequiredMixin, DeleteView):
    model = Playlist
    template_name = 'playlist/delete.html'
    success_url = reverse_lazy('app_user_playlists')
