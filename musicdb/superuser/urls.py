from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^superuser$', views.view,
        name='view'),
)
