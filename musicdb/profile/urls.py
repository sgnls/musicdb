from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('musicdb.profile.views',
    url(r'^profile$', 'view',
        name='nonclassical'),
)
