from django.conf.urls.defaults import *

from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'musicdb.views.index',
        name='home'),

    url(r'', include('musicdb.auth.urls', namespace='auth')),
    url(r'', include('musicdb.profile.urls', namespace='profile')),

    url(r'^classical/', include('musicdb.classical.urls')),
    url(r'^albums/', include('musicdb.nonclassical.urls')),
    url(r'^common/', include('musicdb.common.urls')),
    url(r'^unfiled/', include('musicdb.unfiled.urls', namespace='unfiled')),

    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url('^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': '../media',
        }),
        url('^site_media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': 'site_media',
        }),
    )
