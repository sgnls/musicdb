from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('musicdb.classical.classical_unfiled.views',
    url(r'^classical/unfiled/(?P<path>.+/)?$', 'view',
        name='view'),
)
