from django.http import HttpResponse,HttpResponseNotFound

from django.shortcuts import render

# Create your views here.
def home_page(request):
    return HttpResponse("Home page of website blog")
def blogposts(request):
    return  HttpResponse("all blog posts!")


def blog_post(request, blog):
    if blog=='python-intro':
        res = "python blog posts!"
    elif blog=='django-basics':
        res = "django blog posts!"
    else:
        return HttpResponseNotFound('Blog not found')

    return HttpResponse(res)

def blog_post_by_number(request, blog):
    return HttpResponse(blog)  