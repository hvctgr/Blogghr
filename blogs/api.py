from django.db.models import Q
from django.utils import timezone
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blogs.models import Post
from blogs.permissions import PostPermission
from blogs.serializers import PostListSerializer, PostSerializer


class PostsAPI(ListCreateAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-publication_date')
        if self.request.user.is_anonymous:
            return queryset.filter(Q(publication_date__lte=timezone.now()))
        elif self.request.user.is_superuser:
            return queryset
        else:  # is an authenticated user
            return queryset.filter(Q(owner=self.request.user) | Q(publication_date__lte=timezone.now()))

    def get_serializer_class(self):
        return PostListSerializer if self.request.method == 'GET' else PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailAPI(RetrieveUpdateDestroyAPIView):

    permission_classes = [PostPermission]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)