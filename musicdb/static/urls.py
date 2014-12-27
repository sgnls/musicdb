from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('musicdb.static.views',
    url(r'^$', 'landing',
        name='landing'),
)
