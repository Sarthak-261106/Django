from django.http import HttpResponse,HttpResponseNotFound

from django.shortcuts import render

# Create your views here.

blog_names={'python-intro':"python blog posts!",'django-basics':"django blog posts!",'regex':'regular expressions'}

def home_page(request):
    return HttpResponse("<h1>Home page of website blog</h1>")


def blogposts(request):
    res_data="""
    <u1>
        <li><a href="allposts/python-intro">Python Intro</a></li>
        <li><a href="allposts/django-basics">Django basics</a></li>
        <li><a href="allposts/regex">REGEX</a></li>
        
    </u1>
    """
    return  HttpResponse(res_data)


def blog_post(request, blog):
    # if blog=='python-intro':
    #     res = "python blog posts!"
    # elif blog=='django-basics':
    #     res = "django blog posts!"
    # else:
    try:
        res=blog_names[blog]
    except Exception:
        return HttpResponseNotFound('Blog not found')
    else:
        return HttpResponse(res)

def blog_post_by_number(request, blog):
    return HttpResponse(blog)