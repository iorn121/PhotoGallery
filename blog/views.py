from django.shortcuts import render
from .models import Blog


def index(request):
    blogs = Blog.objects.order_by('-created_at')
    return render(request, 'blog/index.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
