from django.shortcuts import render
from django.http import HHTPResponse
# Create your views here.

def blogs(request):
    return HHTPResponse(request,'MY BLOG DATA')
