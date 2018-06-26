from django.conf.urls import url
from Post import views

urlpatterns = [
    url(r'^post/$', views.post_list),
    url(r'^comment/$', views.comment_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_list),
]