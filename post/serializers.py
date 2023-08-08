from rest_framework import serializers
from core.models import Post
from user.serializers import UserSerializer
from django.contrib.auth import (
    get_user_model,
    authenticate,
)


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Post
        fields = '__all__'

