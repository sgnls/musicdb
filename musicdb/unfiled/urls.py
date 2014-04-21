from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('musicdb.unfiled.views',
    url(r'^unfiled/(?P<path>.+/)?$', 'view',
        name='view'),
)
