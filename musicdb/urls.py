from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'', include('musicdb.auth.urls', namespace='auth')),
    url(r'', include('musicdb.books.urls', namespace='books')),
    url(r'', include('musicdb.classical.urls', namespace='classical')),
    url(r'', include('musicdb.common.urls', namespace='common')),
    url(r'', include('musicdb.debug.urls', namespace='debug')),
    url(r'', include('musicdb.albums.urls', namespace='albums')),
    url(r'', include('musicdb.profile.urls', namespace='profile')),
    url(r'', include('musicdb.static.urls', namespace='static')),
    url(r'', include('musicdb.superuser.urls', namespace='superuser')),
)
