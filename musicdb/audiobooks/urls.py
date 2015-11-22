from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('musicdb.audiobooks.views',
    url(r'^audiobooks$', 'view',
        name='view'),
    url(r'^audiobooks/(?P<letter>[a-z-0])$', 'view',
        name='view'),
    url(r'^audiobooks/(?P<slug>[^/]+)$', 'author',
        name='author'),

    url(r'^audiobooks/play/(?P<audiobook_id>[^/]+).m3u$', 'play',
        name='play'),
    url(r'^audiobooks/play/(?P<audiobook_id>[^/]+).rss$', 'rss',
        name='rss'),
)
