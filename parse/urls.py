from django.conf.urls import patterns, url

from parse import views

urlpatterns = patterns('',
    url(r'^$', views.parse, name='index'),
)