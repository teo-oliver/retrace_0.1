from django.contrib import admin
from django.urls import path

from .views import (PostListView, 
                    PostDetailView, 
                    PostCreateView, 
                    PostUpdateView, 
                    PostDeleteView)

# app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post_update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    path('post/new/', PostCreateView.as_view(), name="post_create"), 
]
