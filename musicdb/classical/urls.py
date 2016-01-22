from django.conf.urls import url, include

from . import views

urlpatterns = (
    url(r'', include('musicdb.classical.classical_unfiled.urls',
        namespace='unfiled')),

    url(r'^classical$', views.view,
        name='view'),

    url(r'^classical/artists$', views.artists,
        name='artists'),
    url(r'^classical/artists/(?P<slug>[^/]+)$', views.artist,
        name='artist'),
    url(r'^classical/artists/(?P<artist_slug>[^/]+)/(?P<slug>[^/]+)$', views.work,
        name='work'),

    url(r'^classical/ensembles$', views.ensembles,
        name='ensembles'),
    url(r'^classical/ensembles/(?P<slug>[^/]+)$', views.ensemble,
        name='ensemble'),

    url(r'^classical/play/recording/(?P<recording_id>\d+)/play$', views.play_recording,
        name='play-recording'),
)
