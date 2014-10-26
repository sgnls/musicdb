from django.conf.urls import patterns, url

urlpatterns = patterns('musicdb.auth.auth_admin.views',
    url(r'^superuser/users$', 'view',
        name='view'),
)
