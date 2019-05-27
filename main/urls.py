"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from blogs.api import PostsAPI, PostDetailAPI, BlogsAPI
from blogs.views import LatestPost, BlogList, BlogDetail, BlogPostDetail, NewPostView
from users.api import UsersAPI, UserDetailAPI
from users.views import LoginView, LogoutView, SignupView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Users
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', SignupView.as_view(), name='signup'),

    # Blogs
    path('blogs/', BlogList.as_view(), name='blog_list'),
    path('blogs/<str:username>/', BlogDetail.as_view(), name='blog_detail'),
    path('blogs/<str:username>/<int:pk>', BlogPostDetail.as_view(), name='blog_post_detail'),
    path('new-post/', NewPostView.as_view(), name='new_post'),
    path('', LatestPost.as_view(), name='home'),

    # API
    path('apiv1/users/<int:pk>/', UserDetailAPI.as_view(), name='user_detail_api'),
    path('apiv1/users/', UsersAPI.as_view(), name='users_api'),
    path('apiv1/posts/<int:pk>', PostDetailAPI.as_view(), name='post_detail_api'),
    path('apiv1/posts/', PostsAPI.as_view(), name='posts_api'),
    path('apiv1/blogs/', BlogsAPI.as_view(), name='blogs_api')
]
