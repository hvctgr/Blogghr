from django.forms import ModelForm

from blogs.models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['name', 'description', 'content', 'url', 'categories', 'publication_date']
