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
