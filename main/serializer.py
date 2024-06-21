from pip._vendor.packaging.tags import Tag
from rest_framework import serializers

from .models import *

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('url', 'id', 'name')

class AboutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = About
        fields = ('url', 'id', 'title', 'description')
        read_only_fields = ('url', 'id', 'title', 'description')
        write_only_fields = ('url', 'id', 'title', 'description')

