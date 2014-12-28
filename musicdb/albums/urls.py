from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('musicdb.albums.views',
    # settings.LOGIN_REDIRECT_URL
    url(r'^albums$', 'view',
        name='view'),
    url(r'^albums/(?P<letter>[a-z-0])$', 'view',
        name='view'),

    url(r'^albums/(?P<slug>[^/]+)$', 'artist',
        name='artist'),
    url(r'^albums/(?P<artist_slug>[^/]+)/(?P<slug>[^/]+)$', 'album',
        name='album'),
    url(r'^albums/play/album/(?P<album_id>\d+)$', 'play_album',
        name='play-album'),
    url(r'^albums/play/album/(?P<album_id>\d+)/cd/(?P<cd_id>\d+)$', 'play_cd',
        name='play-cd'),
)
