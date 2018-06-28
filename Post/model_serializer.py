from django.contrib.auth.models import User
from rest_framework import serializers
from Post.models import Post, Comment, Like


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class LikeSerializer(serializers.ModelSerializer):

    def like(self):
        validated_data = self.validated_data
        obj, created = Like.objects.get_or_create(**validated_data)
        if not created:
            obj.delete()
        return created

    class Meta:
        model = Like
        fields = '__all__'

