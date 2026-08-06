from django.http import HttpResponse,HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render

# Create your views here.

blog_names={'python-intro':"python blog posts!",'django-basics':"django blog posts!",'regex':'regular expressions'}

def home_page(request):
    return render(request,'blogs/index.html')
    # res_data=render_to_string("blogs/index.html")
    # return HttpResponse(res_data)


def blogposts(request):
    list_items=''
    blog_list=list(blog_names.keys())
    for b in blog_list:
        blog_path=reverse('blog-post',args=[b])
        list_items+=f'<li><a href="{blog_path}">{b.capitalize()}</a></li>'


    res_data=f"<ul>{list_items}</ul>"
    return  HttpResponse(res_data)


def blog_post(request, blog):
    # if blog=='python-intro':
    #     res = "python blog posts!"
    # elif blog=='django-basics':
    #     res = "django blog posts!"
    # else:
    try:
        res=blog_names[blog]
        return render(request,'blogs/posts.html',{"blog_text":res})
    except Exception:
        return HttpResponseNotFound('Blog not found')
    # else:
    #     return HttpResponse(res)

def blog_post_by_number(request, blog):
    return HttpResponse(blog)