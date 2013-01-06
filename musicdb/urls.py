from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'musicdb.views.index',
        name='home'),

    url(r'', include('musicdb.auth.urls', namespace='auth')),
    url(r'', include('musicdb.classical.urls')),
    url(r'', include('musicdb.common.urls')),
    url(r'', include('musicdb.debug.urls', namespace='debug')),
    url(r'', include('musicdb.nonclassical.urls')),
    url(r'', include('musicdb.profile.urls', namespace='profile')),
    url(r'', include('musicdb.unfiled.urls', namespace='unfiled')),

    (r'^admin/', include(admin.site.urls)),
)
