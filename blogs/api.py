from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from blogs.models import Post
from blogs.serializers import PostListSerializer, PostSerializer


class PostsAPI(ListCreateAPIView):

    queryset = Post.objects.all()

    def get_serializer_class(self):
        return PostListSerializer if self.request.method == 'GET' else PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailAPI(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
