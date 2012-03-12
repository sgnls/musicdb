from django.conf.urls.defaults import *

urlpatterns = patterns('musicdb.classical.views',
    url(r'^$', 'index',
        name='classical'),

    url(r'^composers/$', 'composers',
        name='classical-composers'),
    url(r'^artists/$', 'artists',
        name='classical-artists'),
    url(r'^ensembles/$', 'ensembles',
        name='classical-ensembles'),

    url(r'^categories/$', 'categories',
        name='classical-categories'),
    url(r'^category/(?P<category_slug>[^/]+)$', 'category',
        name='classical-category'),

    url(r'^stats/$', 'stats',
        name='classical-stats'),
    url(r'^recent$', 'recent',
        name='classical-recent'),

    url(r'^artist/(?P<slug>[^/]+)$', 'artist',
        name='classical-artist'),
    url(r'^artist/(?P<artist_slug>[^/]+)/(?P<slug>[^/]+)$', 'work',
        name='classical-work'),
    url(r'^ensemble/(?P<slug>[^/]+)$', 'ensemble',
        name='classical-ensemble'),

    url(r'^play/recording/(?P<recording_id>\d+).m3u$', 'play_recording',
        name='classical-play-recording'),
)
