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
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    """
    if request.method =='GET':
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
            return post_serializer.instance
        else:
            return JsonResponse(post_serializer.errors, status=404)


@csrf_exempt
def post_detail(request, pk):
    """
        def snippet_detail(request, pk):
        Retrieve, update or delete a code snippet.
        try:
            snippet = Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return HttpResponse(status=404)
    
        if request.method == 'GET':
            serializer = SnippetSerializer(snippet)
            return JsonResponse(serializer.data)
    
        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = SnippetSerializer(snippet, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)
    
        elif request.method == 'DELETE':
            snippet.delete()
            return HttpResponse(status=204)

    """
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



