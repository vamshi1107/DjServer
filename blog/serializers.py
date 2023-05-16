from rest_framework import serializers
from blog.models import Blog, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'name', 'email', 'dp', 'intrest')


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('bid', 'username', 'cover', 'title', 'content',
                  'date', 'topics', 'count', 'duration')
