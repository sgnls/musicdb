from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('musicdb.auth.views',
    url(r'^login$', 'login',
        name='login'),
)
