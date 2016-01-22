from django.conf.urls import url

from . import views

urlpatterns = (
    # settings.LOGIN_REDIRECT_URL
    url(r'^albums$', views.view,
        name='view'),
    url(r'^albums/(?P<letter>[a-z-0])$', views.view,
        name='view'),

    url(r'^albums/(?P<slug>[^/]+)$', views.artist,
        name='artist'),
    url(r'^albums/(?P<artist_slug>[^/]+)/(?P<slug>[^/]+)$', views.album,
        name='album'),
    url(r'^albums/play/album/(?P<album_id>\d+)$', views.play_album,
        name='play-album'),
    url(r'^albums/play/album/(?P<album_id>\d+)/cd/(?P<cd_id>\d+)$', views.play_cd,
        name='play-cd'),
)
