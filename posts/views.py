from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
                                  
from .models import Post



class PostListView(ListView):
    model = Post
    template_name = 'blog/blog_home.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Board', }
    ordering = ['-date_posted']
    paginate_by = 4


class PostDetailView(DetailView):
    model = Post
    # template_name = 'blog/blog_detail.html'
    # context_object_name = 'posts'
    extra_context = {'title': 'Detail', }


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    extra_context = {'title': 'Create', }
    # success_url = 'home-blog'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    extra_context = {'title': 'Create', }
    # success_url = 'home-blog'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    extra_context = {'title': 'Detail', }
    success_url = '/blog/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
