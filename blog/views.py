from django.http import HttpResponseServerError
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render
from .models import Blog


def index(request):
    blogs = Blog.objects.order_by('-created_at')
    return render(request, 'blog/index.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})


@requires_csrf_token
def my_customized_server_error(request, template_name='500.html'):
    import sys
    from django.views import debug
    error_html = debug.technical_500_response(request, *sys.exc_info()).content
    return HttpResponseServerError(error_html)
