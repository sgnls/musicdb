from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('musicdb.classical.views',
    url(r'^classical$', 'composers',
        name='composers'),
    url(r'^classical/artists$', 'artists',
        name='artists'),
    url(r'^classical/ensembles$', 'ensembles',
        name='ensembles'),

    url(r'^classical/artist/(?P<slug>[^/]+)$', 'artist',
        name='artist'),
    url(r'^classical/artist/(?P<artist_slug>[^/]+)/(?P<slug>[^/]+)$', 'work',
        name='work'),
    url(r'^classical/ensemble/(?P<slug>[^/]+)$', 'ensemble',
        name='ensemble'),

    url(r'^classical/play/recording/(?P<recording_id>\d+)/play$', 'play_recording',
        name='play-recording'),
)
