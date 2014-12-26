from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('musicdb.nonclassical.views',
    url(r'^albums/$', 'index',
        name='view'),
    url(r'^albums/(?P<letter>[a-z-0])$', 'index',
        name='letter'),
    url(r'^albums/(?P<slug>[^/]+)$', 'artist',
        name='artist'),
    url(r'^albums/(?P<artist_slug>[^/]+)/(?P<slug>[^/]+)$', 'album',
        name='album'),
    url(r'^albums/play/album/(?P<album_id>\d+)$', 'play_album',
        name='play-album'),
    url(r'^albums/play/cd/(?P<cd_id>\d+)$', 'play_cd',
        name='play-cd'),
)
