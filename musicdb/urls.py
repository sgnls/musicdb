from django.conf import settings
from django.conf.urls import include, url
from django.views.static import serve

urlpatterns = (
    url(r'', include('musicdb.account.urls',
        namespace='account')),
    url(r'', include('musicdb.audiobooks.urls',
        namespace='audiobooks')),
    url(r'', include('musicdb.books.urls',
        namespace='books')),
    url(r'', include('musicdb.classical.urls',
        namespace='classical')),
    url(r'', include('musicdb.common.urls',
        namespace='common')),
    url(r'', include('musicdb.albums.urls',
        namespace='albums')),
    url(r'', include('musicdb.profile.urls',
        namespace='profile')),
    url(r'', include('musicdb.static.urls',
        namespace='static')),
    url(r'', include('musicdb.superuser.urls',
        namespace='superuser')),
)

if settings.DEBUG:
    urlpatterns += (
        url(r'^storage/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
