from django.conf.urls import url, include
from django.urls import path

from Post import views, GenericViews

urlpatterns = [

    # List All Comments for Post Given id.
    url(r'^comments/(?P<pk>[0-9]+)/$', GenericViews.CommentList.as_view()),

    # GET, PUT for Post given id.
    url(r'^post/(?P<pk>[0-9]+)/$', GenericViews.PostDetail.as_view()),

    # Update, GET, DELETE Comment given id.
    path('comment/<int:pk>/', GenericViews.CommentDetail.as_view()),

    # CREATE, DELETE Like given post id.
    path('post/<int:pk>/like/', GenericViews.CreateDestroyLikeView.as_view()),

    # List All Posts
    path('', GenericViews.PostList.as_view()),

]

