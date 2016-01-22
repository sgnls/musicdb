from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^common/play/(?P<music_file_id>\d+)$', views.play_music_file,
        name='play-music-file'),
)
