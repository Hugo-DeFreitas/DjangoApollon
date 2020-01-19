from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core import serializers
from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView

from app.forms.playlist import PlaylistForm
from app.models import Playlist, UserProfile, Song


class PlaylistCreate(LoginRequiredMixin, CreateView):
    model = Playlist
    template_name = 'playlist/create.html'
    success_url = reverse_lazy('app_user_playlists')
    form_class = PlaylistForm

    def form_valid(self, form):
        if not form.is_valid():
            return False
        self.object = form.save()
        self.object.created_by = UserProfile.objects.get(user=self.request.user)
        return super().form_valid(form)


class PlaylistList(LoginRequiredMixin, ListView):
    template_name = 'playlist/list.html'
    model = Playlist

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['playlists_followed'] = Playlist.objects.filter(followers__user=self.request.user)
        return context

    def get_queryset(self):
        return Playlist.objects.filter(created_by__user_id=self.request.user.id)


class PlaylistDetail(LoginRequiredMixin, DetailView):
    template_name = 'playlist/detail.html'
    model = Playlist
    slug_url_kwarg = 'not_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_playlists'] = Playlist.objects.filter(created_by=UserProfile.objects.get(user=self.request.user))
        return context


class PlaylistUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.get_object().created_by.user == self.request.user

    model = Playlist
    template_name = 'playlist/update.html'
    success_url = reverse_lazy('app_home')
    form_class = PlaylistForm


class PlaylistDelete(LoginRequiredMixin, DeleteView):
    model = Playlist
    template_name = 'playlist/delete.html'
    success_url = reverse_lazy('app_user_playlists')


@login_required
def follow_playlist(request):
    if request.is_ajax():
        # Si on renvoit un objet de type 'None', vu qu'il n'est pas serializable, on lance une erreur 500.
        if not request.POST.get('playlist_id'):
            return JsonResponse(None)
        playlistToUpdate = Playlist.objects.get(pk=request.POST.get('playlist_id'))
        if not playlistToUpdate:
            return JsonResponse(None)
        playlistToUpdate.followers.add(UserProfile.objects.get(user=request.user))
        return JsonResponse(serializers.serialize('json', [playlistToUpdate, ]), safe=False)

    if not request.GET.get('playlist_id'):
        return HttpResponseNotFound()
    playlistToUpdate = Playlist.objects.get(pk=request.GET.get('playlist_id'))
    if not playlistToUpdate:
        return HttpResponseNotFound()
    playlistToUpdate.followers.add(UserProfile.objects.get(user=request.user))
    return redirect(reverse_lazy('app_user_playlists'))


@login_required
def unfollow_playlist(request):
    if request.is_ajax():
        # Si on renvoit un objet de type 'None', vu qu'il n'est pas serializable, on lance une erreur 500.
        if not request.POST.get('playlist_id'):
            return JsonResponse(None)
        playlistToUpdate = Playlist.objects.get(pk=request.POST.get('playlist_id'))
        if not playlistToUpdate:
            return JsonResponse(None)
        playlistToUpdate.followers.remove(UserProfile.objects.get(user=request.user))
        return JsonResponse(serializers.serialize('json', [playlistToUpdate, ]), safe=False)

    if not request.GET.get('playlist_id'):
        return HttpResponseNotFound()
    playlistToUpdate = Playlist.objects.get(pk=request.GET.get('playlist_id'))
    if not playlistToUpdate:
        return HttpResponseNotFound()
    playlistToUpdate.followers.remove(UserProfile.objects.get(user=request.user))
    return redirect(reverse_lazy('app_user_playlists'))

@login_required
def delete_song_from_playlist(request):
    if request.is_ajax():
        # Si on renvoit un objet de type 'None', vu qu'il n'est pas serializable, on lance une erreur 500.
        if not request.POST.get('playlist_id') or not request.POST.get('song_id'):
            return JsonResponse(None)
        playlistToUpdate = Playlist.objects.get(pk=request.POST.get('playlist_id'))
        songToDelete = Song.objects.get(pk=request.POST.get('song_id'))
        if not playlistToUpdate or not songToDelete:
            return JsonResponse(None)

        playlistToUpdate.songs.remove(songToDelete)

        return JsonResponse(serializers.serialize('json', [playlistToUpdate, ]), safe=False)