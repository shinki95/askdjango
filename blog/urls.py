# _*_ coding: utf-8 _*_

from django.conf.urls import url
from . import views
from . import views_cbv

urlpatterns = [
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^$', views_cbv.post_list, name='post_list'),
    url(r'^(?P<pk>\d+)/$', views_cbv.post_detail, name='post_detail'),
    url(r'^(?P<id>\d+)/edit/$', views.post_edit, name='post_edit'),
    #url(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^$', views.post_list, name="post_list"),
    url(r'^hello/(?P<name>[ㄱ-힣a-zA-Z]+)/(?P<company>[ㄱ-힣a-zA-Z]+)/$', views.hello),
]

