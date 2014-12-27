from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('musicdb.common.views',
    url(r'^common/play/(?P<music_file_id>\d+)$', 'play_music_file',
        name='play-music-file'),
)
