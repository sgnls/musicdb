from django.conf.urls import url, include

from . import views

urlpatterns = (
    url(r'', include('musicdb.books.books_admin.urls',
        namespace='admin')),

    url(r'^books$', views.view,
        name='view'),
    url(r'^books/(?P<letter>[a-z-0])$', views.view,
        name='view'),
    url(r'^books/(?P<slug>[^/]+)$', views.author,
        name='author'),

    url(r'^books/mobi/email/(?P<mobi_file_id>\d+)$', views.mobi_email,
        name='mobi-email'),
    url(r'^books/mobi/download/(?P<mobi_file_id>\d+)$', views.mobi_download,
        name='mobi-download'),
)
