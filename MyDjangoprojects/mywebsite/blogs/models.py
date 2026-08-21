from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    preview = models.CharField(max_length=250)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    image = models.CharField(max_length=50)


