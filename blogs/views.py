import datetime

from django.shortcuts import render

from django.views.generic import ListView

from blogs.models import Post


class LatestPost(ListView):
    template_name = 'blogs/latest.html'

    def get_queryset(self):
        queryset = Post.objects.filter(publication_date__lte=datetime.datetime.now()).order_by('-publication_date')
        return queryset


