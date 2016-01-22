from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^classical/unfiled/(?P<path>.+/)?$', views.view,
        name='view'),
)
