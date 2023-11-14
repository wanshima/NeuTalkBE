from rest_framework import serializers
from .models import CustomUser
from .models import Post, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

from rest_framework import serializers
from .models import Post  # Ensure Post model is correctly imported

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['post_id', 'title', 'content', 'author', 'created_at']  # Adjust fields as necessary

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post_id', 'content', 'author', 'created_at']