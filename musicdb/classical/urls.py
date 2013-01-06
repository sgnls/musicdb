from django.conf.urls.defaults import *

urlpatterns = patterns('musicdb.classical.views',
    url(r'^classical/$', 'index',
        name='classical'),

    url(r'^classical/composers/$', 'composers',
        name='classical-composers'),
    url(r'^classical/artists/$', 'artists',
        name='classical-artists'),
    url(r'^classical/ensembles/$', 'ensembles',
        name='classical-ensembles'),

    url(r'^classical/categories/$', 'categories',
        name='classical-categories'),
    url(r'^classical/category/(?P<category_slug>[^/]+)$', 'category',
        name='classical-category'),

    url(r'^classical/stats/$', 'stats',
        name='classical-stats'),
    url(r'^classical/recent$', 'recent',
        name='classical-recent'),

    url(r'^classical/artist/(?P<slug>[^/]+)$', 'artist',
        name='classical-artist'),
    url(r'^classical/artist/(?P<artist_slug>[^/]+)/(?P<slug>[^/]+)$', 'work',
        name='classical-work'),
    url(r'^classical/ensemble/(?P<slug>[^/]+)$', 'ensemble',
        name='classical-ensemble'),

    url(r'^classical/play/recording/(?P<recording_id>\d+).m3u$', 'play_recording',
        name='classical-play-recording'),
)
