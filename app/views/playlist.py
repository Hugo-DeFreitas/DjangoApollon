from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.views.generic import DetailView, ListView

from app.models import Playlist


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
