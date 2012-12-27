from django.conf import settings
from django.conf.urls.defaults import patterns, url

urlpatterns = []

if settings.DEBUG:
    urlpatterns += patterns('musicdb.debug.views',
        url('^media/(?P<path>.*)$', 'media'),
    )
