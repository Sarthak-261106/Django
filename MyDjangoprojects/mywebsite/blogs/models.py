from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_addr = models.EmailField()

class Tag(models.Model):
    caption = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=100)
    preview = models.CharField(max_length=250)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    image = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)



