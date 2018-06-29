from django.contrib.auth.models import User
from rest_framework import serializers
from Post.models import Post, Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if request.user.is_superuser:
            return fields
        if request.method == 'POST':
            fields.pop('archived')
            fields.pop('published')
        elif request.method == 'PUT':
            fields.pop('published')
            if request.user == self.instance.author:
                return fields
            fields.pop('archived')
        return fields

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'comments')
        # write_only_fields = ('id', )


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

