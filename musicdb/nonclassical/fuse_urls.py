from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('musicdb.nonclassical.views',
    url(r'^$', 'fuse_index'),
    url(r'^/(?P<dir_name>[^/]+)$', 'fuse_artist'),
    url(r'^/(?P<artist_dir_name>[^/]+)/(?P<dir_name>[^/]+)$', 'fuse_album'),
    url(r'^/(?P<artist_dir_name>[^/]+)/(?P<album_dir_name>[^/]+)/(?P<dir_name>[^/]+)$', 'fuse_track'),
)
