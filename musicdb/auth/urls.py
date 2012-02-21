from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('musicdb.auth.views',
    url(r'^login$', 'login',
        name='login'),
    url(r'^logout$', 'logout',
        name='logout'),
    url(r'^password$', 'change_password',
        name='change-password'),
)
