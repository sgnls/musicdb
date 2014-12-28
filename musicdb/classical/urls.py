from django.conf.urls.defaults import url, patterns, include

urlpatterns = patterns('musicdb.classical.views',
    url(r'', include('musicdb.classical.classical_unfiled.urls', namespace='unfiled')),

    url(r'^classical$', 'view',
        name='view'),

    url(r'^classical/artists$', 'artists',
        name='artists'),
    url(r'^classical/artists/(?P<slug>[^/]+)$', 'artist',
        name='artist'),
    url(r'^classical/artists/(?P<artist_slug>[^/]+)/(?P<slug>[^/]+)$', 'work',
        name='work'),

    url(r'^classical/ensembles$', 'ensembles',
        name='ensembles'),
    url(r'^classical/ensembles/(?P<slug>[^/]+)$', 'ensemble',
        name='ensemble'),

    url(r'^classical/play/recording/(?P<recording_id>\d+)/play$', 'play_recording',
        name='play-recording'),
)
