from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('musicdb.books.views',
    (r'', include('musicdb.books.books_admin.urls', namespace='admin')),

    url(r'^books$', 'view',
        name='view'),
    url(r'^books/(?P<letter>[a-z-0])$', 'view',
        name='view'),
    url(r'^books/(?P<slug>[^/]+)$', 'author',
        name='author'),
    url(r'^books/download/(?P<book_id>\d+)$', 'book',
        name='book'),
)
