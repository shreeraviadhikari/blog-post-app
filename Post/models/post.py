from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(User, related_name='all_posts', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title[:20]


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='comment')
    content = models.TextField()

    def __str__(self):
        return self.content[:20]

