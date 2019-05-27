from django.db.models import Q
from django.utils import timezone
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blogs.models import Post
from blogs.permissions import PostPermission
from blogs.serializers import PostListSerializer, PostSerializer, BlogSerializer


class PostsAPI(ListCreateAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'content']
    ordering_fields = ['name', 'publication_date']

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


class BlogsAPI(ListAPIView):
    from django.contrib.auth.models import User

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['username']
    ordering_fields = ['username']

    serializer_class = BlogSerializer
    queryset = User.objects.all()
