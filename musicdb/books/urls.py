from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('musicdb.books.views',
    url(r'^books$', 'index',
        name='index'),
    url(r'^books/(?P<letter>[a-z-0])$', 'index',
        name='index'),
    url(r'^books/(?P<slug>[^/]+)$', 'author',
        name='author'),
)
