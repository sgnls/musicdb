from django.conf.urls import patterns, url

urlpatterns = patterns('musicdb.books.books_admin.views',
    url(r'^books/admin/author/(?P<author_id>\d+)$', 'author',
        name='author'),
)
