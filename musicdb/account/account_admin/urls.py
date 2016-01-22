from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^superuser/users$', views.view,
        name='view'),
    url(r'^superuser/users/(?P<user_id>\d+)$', views.user,
        name='user'),
    url(r'^superuser/users/(?P<user_id>\d+)/reset-password$', views.reset_password,
        name='reset-password'),
)
