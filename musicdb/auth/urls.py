from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('musicdb.auth.views',
    (r'', include('musicdb.auth.auth_admin.urls', namespace='admin')),

    url(r'^login$', 'login',
        name='login'),
    url(r'^logout$', 'logout',
        name='logout'),
    url(r'^password$', 'change_password',
        name='change-password'),
)
