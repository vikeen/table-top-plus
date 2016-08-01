from django.conf.urls import url

from . import views

app_name = 'characters'
urlpatterns = [
    url(r'^$', views.index.as_view(), name='index'),
    url(r'^create$', views.create.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/delete$', views.delete.as_view(), name='delete')
]
