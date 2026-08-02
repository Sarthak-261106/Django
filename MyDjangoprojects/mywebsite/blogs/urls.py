from django.urls import path
from . import views
from blogs import views

urlpatterns = [
    path("",views.home_page),
    path('allposts', views.blogposts),
    path("python-intro",views.python_intro),
    path("django-basics",views.django_basics)

]
