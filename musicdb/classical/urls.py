from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('musicdb.classical.views',
    url(r'^classical/$', 'index',
        name='view'),

    url(r'^classical/composers/$', 'composers',
        name='composers'),
    url(r'^classical/artists/$', 'artists',
        name='artists'),
    url(r'^classical/ensembles/$', 'ensembles',
        name='ensembles'),

    url(r'^classical/categories/$', 'categories',
        name='categories'),
    url(r'^classical/category/(?P<category_slug>[^/]+)$', 'category',
        name='category'),

    url(r'^classical/recent$', 'recent',
        name='recent'),

    url(r'^classical/artist/(?P<slug>[^/]+)$', 'artist',
        name='artist'),
    url(r'^classical/artist/(?P<artist_slug>[^/]+)/(?P<slug>[^/]+)$', 'work',
        name='work'),
    url(r'^classical/ensemble/(?P<slug>[^/]+)$', 'ensemble',
        name='ensemble'),

    url(r'^classical/play/recording/(?P<recording_id>\d+).m3u$', 'play_recording',
        name='play-recording'),
)
