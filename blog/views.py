from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class HomePage(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'MyBlog'
        return context

    def get_queryset(self):
        return Post.objects.filter(is_published=True)
