import datetime

from django.contrib.auth.models import User
from django.db import models
# from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    content = models.TextField()
    url = models.URLField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    publication_date = models.DateTimeField(default=datetime.datetime.now)  # o timezone.now(), problema naive
    categories = models.ManyToManyField(Category)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

