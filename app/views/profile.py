from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, DetailView
from django.utils.translation import gettext_lazy as _

from app.forms.profile import ProfileForm
from app.models import UserProfile, Playlist


class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'profile/update.html'
    form_class = ProfileForm
    success_message = _('Your profile was successfully updated')

    def test_func(self):
        return self.get_object() == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        currentProfile = UserProfile.objects.get(user=self.request.user)
        context['profile'] = currentProfile
        return context

    def form_valid(self, form):
        if form.is_valid():
            profile = UserProfile.objects.get(user=self.request.user)
            profile.biography = form.cleaned_data['biography']
            profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('app_profile_update', kwargs={'pk': self.request.user.id})


class PublicProfile(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profile/public-profile.html'
    slug_field = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # On doit l'écraser parce que sur les User Detail Views de User model, l'indice de contexte
        # 'user' avec celui qu'on observe...
        context['user'] = self.request.user
        context['profile'] = UserProfile.objects.get(user=self.object)
        context['playlists_created'] = Playlist.objects.filter(created_by=context['profile'], is_public=True)
        context['total_songs'] = sum([playlist.songs.count() for playlist in context['playlists_created']])
        context['total_follower'] = sum([playlist.followers.count() for playlist in context['playlists_created']])
        return context
