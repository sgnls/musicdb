from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^books/admin/author/(?P<author_id>\d+)$', views.author,
        name='author'),
    url(r'^books/admin/author/(?P<author_id>\d+)/merge$', views.author_merge,
        name='author-merge'),
    url(r'^books/admin/book/(?P<book_id>\d+)$', views.book,
        name='book'),
)
