import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from django.views.generic import ListView, DetailView

from blogs.forms import PostForm
from blogs.models import Post

from django.utils import timezone
now = timezone.now()


class LatestPost(ListView):
    template_name = 'blogs/latest.html'

    def get_queryset(self):
        queryset = Post.objects.filter(publication_date__lte=now).order_by('-publication_date')
        return queryset


class BlogList(ListView):
    template_name = 'blogs/blog_list.html'

    def get_queryset(self):
        queryset = User.objects.all().exclude(username='admin')
        return queryset


class BlogDetail(ListView):
    template_name = 'blogs/blog_detail.html'

    def get_queryset(self):
        queryset = Post.objects.filter(owner__username=self.kwargs.get('username'),
                                       publication_date__lte=now).order_by('-publication_date')
        return queryset

""""
class BlogPostDetail(View):
    def get(self, request, username, pk):
        post = get_object_or_404(Post.objects.select_related('owner'), pk=pk)
        context = {'post': post, 'owner': username}
        html = render(request, 'blogs/blog_post_detail.html', context)
        return HttpResponse(html)
"""


class BlogPostDetail(DetailView):
    template_name = 'blogs/blog_post_detail.html'

    def get_queryset(self):
        queryset = Post.objects.filter(owner__username=self.kwargs.get('username'), pk=self.kwargs.get('pk'),
                                       publication_date__lte=now)
        return queryset


class NewPostView(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        context = {'form': form}
        return render(request, 'blogs/new_post.html', context)

    def post(self, request):
        post = Post()
        post.owner = request.user
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save()
            messages.success(request, 'Post creado correctamente con ID {0}'.format(new_post.pk))
            form = PostForm()

        context = {'form': form}
        return render(request, 'blogs/new_post.html', context)
