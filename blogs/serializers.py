from django.urls import reverse
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from blogs.models import Post


class PostListSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'name', 'description', 'url', 'publication_date']


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'name', 'description', 'content', 'url', 'creation_date', 'modification_date',
                  'publication_date', 'categories', 'owner']
        read_only_fields = ['id', 'creation_date', 'modification_date', 'owner']


class BlogSerializer(serializers.Serializer):

    username = serializers.ReadOnlyField()
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        blog_url = reverse('blog_detail', args=[obj.username])
        return blog_url
