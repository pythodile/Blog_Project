from django.db import models
from posts.models import Post
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    commented_by = models.ForeignKey(User, on_delete= models.CASCADE)
    post = models.ManyToManyField(Post)
    content = models.TextField()


