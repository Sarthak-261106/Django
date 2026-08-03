from django.urls import path
from . import views
from blogs import views

urlpatterns = [
    path("",views.home_page),
    path('allposts', views.blogposts),
    path("allposts/<slug:blog>",views.blog_post)
]

