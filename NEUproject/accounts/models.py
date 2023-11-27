from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):

    # Add custom fields here, if needed

    def __str__(self):
        return self.username

from django.db import models
import uuid

class Post(models.Model):
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    post_id = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'

    # def save(self, *args, **kwargs):
    #     if not self.comment_id:
    #         self.comment_id = custom_uuid_function()  # Implement this function
    #     super().save(*args, **kwargs)