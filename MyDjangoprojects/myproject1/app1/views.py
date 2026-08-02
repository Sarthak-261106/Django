from django.shortcuts import render
from django.http import HttpResponse

def blogs(request):
    return HttpResponse(request,"Hello Blogs")
