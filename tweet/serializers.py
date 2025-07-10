from rest_framework import serializers
from .models import Tweet
from django.contrib.auth.models import User

class TweetSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Tweet
        fields = ['id', 'user', 'username', 'text', 'photo', 'created_at' ]
        read_only_fields = ['id', 'created_at', 'user']


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email']  