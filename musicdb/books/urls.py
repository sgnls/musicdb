from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('musicdb.books.views',
    url(r'^books$', 'index',
        name='index'),
)
