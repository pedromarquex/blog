from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    lead = models.TextField(max_length=300, null=True, blank=True)
    content = models.TextField(max_length=1000)
    photo = models.ImageField(upload_to='post/img', null=True, blank=True)

    def __str__(self):
        return self.title
