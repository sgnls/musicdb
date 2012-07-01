from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('musicdb.unfiled.views',
    url(r'^$', 'view',
        name='view'),
    url(r'^play$', 'play',
        name='play'),
)
