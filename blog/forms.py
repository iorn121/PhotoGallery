from django.forms import ModelForm

from cloudinary.forms import CloudinaryJsFileField

from .models import Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog


class BlogDirectForm(BlogForm):
    image = CloudinaryJsFileField()
