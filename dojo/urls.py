from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^new/$', views.post_new),
url(r'^(?P<pk>\d+)/$', views.post_detail),
url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello),
url(r'^list1/$', views.post_list1),
url(r'^list2/$', views.post_list2),
url(r'^list3/', views.post_list3),
]