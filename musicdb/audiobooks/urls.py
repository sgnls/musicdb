from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('musicdb.audiobooks.views',
    url(r'^audiobooks$', 'view',
        name='view'),
    url(r'^audiobooks/(?P<letter>[a-z-0])$', 'view',
        name='view'),
    url(r'^audiobooks/(?P<slug>[^/]+)$', 'author',
        name='author'),

    url(r'^audiobooks/play/(?P<signed_audiobook_id>[^.]+).xspf$', 'play',
        name='play'),
)
