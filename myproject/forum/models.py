from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)

# class Thread(models.Model):
#     title = models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Thread(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default="Default Content")  
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, default='Default Category')

class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)