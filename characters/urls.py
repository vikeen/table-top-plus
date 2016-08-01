from django.conf.urls import url

from . import views

app_name = 'characters'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^create$', views.Create.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', views.Update.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete$', views.Delete.as_view(), name='delete')
]
