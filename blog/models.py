from django.db import models
from cloudinary.models import CloudinaryField


class Blog(models.Model):
    title = models.CharField(blank=False, null=False, max_length=100)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='image/')
    # image = CloudinaryField('image', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
