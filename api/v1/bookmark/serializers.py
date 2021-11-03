from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Bookmark

class BookmarkSerializer(serializers.ModelSerializer):
    """ Serializer for the model Bookmark """
    title = serializers.CharField(max_length=255)
    url = serializers.URLField()
    is_public = serializers.BooleanField(default=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Bookmark
        fields = ['id', 'user', 'title', 'url', 'is_public', 'created_at']
