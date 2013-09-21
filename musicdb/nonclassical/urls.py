from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('musicdb.nonclassical.views',
    url(r'^albums/$', 'index',
        name='nonclassical'),
    url(r'^albums/collage$', 'collage',
        name='nonclassical-collage'),
    url(r'^albums/(?P<letter>[a-z-0])$', 'index',
        name='nonclassical-letter'),
    url(r'^albums/(?P<slug>[^/]+)$', 'artist',
        name='nonclassical-artist'),
    url(r'^albums/(?P<artist_slug>[^/]+)/(?P<slug>[^/]+)$', 'album',
        name='nonclassical-album'),
    url(r'^albums/play/cd/(?P<cd_id>\d+)$', 'play_cd',
        name='nonclassical-play-cd'),
    url(r'^albums/play/album/(?P<album_id>\d+)$', 'play_album',
        name='nonclassical-play-album'),
)
