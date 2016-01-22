from django.conf.urls import url, include

from . import views

urlpatterns = (
    url(r'', include('musicdb.account.account_admin.urls',
        namespace='admin')),

    url(r'^login$', views.login,
        name='login'),
    url(r'^logout$', views.logout,
        name='logout'),
    url(r'^password$', views.change_password,
        name='change-password'),
)
