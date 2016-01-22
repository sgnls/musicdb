from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^audiobooks$', views.view,
        name='view'),
    url(r'^audiobooks/(?P<letter>[a-z-0])$', views.view,
        name='view'),
    url(r'^audiobooks/(?P<slug>[^/]+)$', views.author,
        name='author'),

    url(r'^audiobooks/play/(?P<signed_audiobook_id>[^/]+).rss$', views.play,
        {'format_': 'rss'}, name='rss'),
    url(r'^audiobooks/play/(?P<signed_audiobook_id>[^.]+).xspf$', views.play,
        {'format_': 'xspf'}, name='xspf'),
)
