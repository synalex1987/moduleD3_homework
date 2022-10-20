from datetime import datetime
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.


class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'post_list'

    #queryset = Post.objects.order_by('-rating') & Post.objects.filter(post_type = 'NS')
    #queryset = Post.objects.order_by('-rating')
    #queryset = Post.objects.order_by('author', '-rating')
    queryset = Post.objects.order_by('-time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name: str = 'post'


class NewsList(ListView):
    model: Post
    template_name = 'news_list.html'
    context_object_name = 'news_list'

    queryset = Post.objects.filter(
        post_type='NS') & Post.objects.order_by('-time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name: str = 'news'

    queryset = Post.objects.filter(post_type='NS')
