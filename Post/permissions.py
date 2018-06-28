from rest_framework import permissions

from Post.models import Comment, Post, Like


class IsOwner(permissions.BasePermission):
    """
    Permission to check if the object
    """
    def has_object_permission(self, request, view, obj):
        # Treating Post and Comments differently
        if isinstance(obj, Comment) or isinstance(obj, Like):
            comment_owner = obj.author == request.user
            post_owner = obj.post.author == request.user
            return comment_owner | post_owner
        elif isinstance(obj, Post):
            post_owner = obj.author == request.user
            return post_owner
        return False

