from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('musicdb.static.views',
    url(r'^$', 'index',
        name='home'),
)
