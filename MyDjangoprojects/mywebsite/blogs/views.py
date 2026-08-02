from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def home_page(request):
    return HttpResponse("Home page of website blog")
def blogposts(request):
    return  HttpResponse("all blog posts!")

def python_intro(request):
    return HttpResponse("python posts!")

def django_basics(request):
    return HttpResponse("Django blog posts!")