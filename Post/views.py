# Response Import

from django.http import JsonResponse, HttpResponse, QueryDict

# import response
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

# For CSRF Tokens
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

# Read/Write JSON
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Model
from Post.models import Post, Comment

# Serializers
from Post.model_serializer import PostSerializer, CommentSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        # List All Posts
        all_posts = Post.objects.all()
        all_posts_serializer = PostSerializer(all_posts, many=True)
        return Response(all_posts_serializer.data)
    elif request.method == 'POST':
        # Save New Post or update
        data = request.data
        post_serializer = PostSerializer(data=data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(post_serializer.errors, status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@api_view(['GET', 'POST'])
def comment_list(request, pk):
    if request.method == 'GET':
        # List All Posts
        post = get_object_or_404(Post, pk=pk)
        all_comments = post.comments.all()
        all_comments_serializer = CommentSerializer(all_comments, many=True)
        return Response(all_comments_serializer.data)
    elif request.method == 'POST':
        # Save New Post or update
        data = request.data
        comment_serializer = CommentSerializer(data=data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data)
        else:
            return Response(comment_serializer.errors, status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        post_serializer = PostSerializer(post)
        return Response(post_serializer.data)
    elif request.method == 'PUT':
        data = request.data
        post_serializer = PostSerializer(post, data=data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

