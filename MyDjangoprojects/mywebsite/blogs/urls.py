from django.urls import path
from . import views
from blogs import views

urlpatterns = [
    path("",views.home_page),
    path('allposts', views.blogposts),
    path("allposts/<int:blog>",views.blog_post_by_number),
    path("allposts/<str:blog>",views.blog_post)
]

