from django.contrib import admin
from Post.models import Post, Comment

admin.site.register([Post, Comment])

