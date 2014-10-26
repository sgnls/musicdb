from django.conf.urls import patterns, url

urlpatterns = patterns('musicdb.superuser.views',
    url(r'^superuser$', 'view',
        name='view'),
)
