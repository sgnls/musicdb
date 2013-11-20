from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('musicdb.unfiled.views',
    url(r'^unfiled/$', 'view',
        name='view'),
    url(r'^unfiled/play$', 'play',
        name='play'),
    url(r'^unfiled/m3u$', 'm3u',
        name='m3u'),
)
