from django.db import models
from django.contrib.auth.models import User
from post.models import Post

# Create your models here.


class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, null=True, blank=True)
    comment_name = models.CharField(max_length=45, default="Anonymous User")
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.text[:30] + "..."
