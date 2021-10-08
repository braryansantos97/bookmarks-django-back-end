from .models import Bookmark
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['id', 'title', 'link']
