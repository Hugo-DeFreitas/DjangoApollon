from django.db.models import Count
from django.views.generic import TemplateView

from app.models import UserProfile, Playlist


class SplashView(TemplateView):
    def get_template_names(self):
        if not self.request.user.is_authenticated:
            return 'layouts/splash.html'
        return 'layouts/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['playlists_trending'] = (Playlist.objects
                                         .annotate(followers_count=Count('followers'))
                                         .order_by('-followers_count'))[:5]
        if self.request.user.is_authenticated:
            context['user_profile'] = UserProfile.objects.get(user=self.request.user)
        return context
