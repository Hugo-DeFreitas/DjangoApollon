from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from app.models import Song

class SongDetail(LoginRequiredMixin, DetailView):
    template_name = 'song/detail.html'
    model = Song

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        songData = self.object.genius_infos.get('response').get('song')
        context['song'] = songData
        return context

