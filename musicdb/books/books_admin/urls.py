from django.conf.urls import patterns, url

urlpatterns = patterns('musicdb.books.books_admin.views',
    url(r'^books/admin/author/(?P<author_id>\d+)$', 'author',
        name='author'),
    url(r'^books/admin/author/(?P<author_id>\d+)/merge$', 'author_merge',
        name='author-merge'),
    url(r'^books/admin/book/(?P<book_id>\d+)$', 'book',
        name='book'),
)
