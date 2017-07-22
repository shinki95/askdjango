# _*_ coding: utf-8 _*_

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new/$', views.post_new),
    url(r'^(?P<id>\d+)/$', views.post_detail),
    url(r'^(?P<id>\d+)/edit/$', views.post_edit),
    url(r'^$', views.post_list),
    url(r'^hello/(?P<name>[ㄱ-힣a-zA-Z]+)/(?P<company>[ㄱ-힣a-zA-Z]+)/$', views.hello),
]