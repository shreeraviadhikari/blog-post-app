# Response Import

from django.http import JsonResponse, HttpResponse

# For CSRF Tokens
from django.views.decorators.csrf import csrf_exempt

# Read/Write JSON
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Model
from Post.models import Post, Comment

# Serializers
from Post.model_serializer import PostSerializer, CommentSerializer


@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        # List All Posts
        all_posts = Post.objects.all()
        all_posts_serializer = PostSerializer(all_posts, many=True)
        return JsonResponse(all_posts_serializer.data, safe=False)
    elif request.method == 'POST':
        # Save New Post or update
        data = JSONParser().parse(request)
        post_serializer = PostSerializer(data=data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse(post_serializer.instance, safe=False)
        else:
            return JsonResponse(post_serializer.errors, status=404)


@csrf_exempt
def comment_list(request):
    if request.method == 'GET':
        # List All Posts
        all_comments = Post.objects.all()
        all_comments_serializer = CommentSerializer(all_comments, many=True)
        return JsonResponse(all_comments_serializer.data, safe=False)
    elif request.method == 'POST':
        # Save New Post or update
        data = JSONParser().parse(request)
        comment_serializer = CommentSerializer(data=data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse(comment_serializer.data, safe=False)
        else:
            return JsonResponse(comment_serializer.errors, status=404)


@csrf_exempt
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        post_serializer = PostSerializer(post)
        return JsonResponse(post_serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        post_serializer = PostSerializer(post, data=data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse(post_serializer.data)
        else:
            return JsonResponse(post_serializer.errors, status=400)
    elif request.method == 'DELETE':
        post.delete()
        return HttpResponse(status=204)

