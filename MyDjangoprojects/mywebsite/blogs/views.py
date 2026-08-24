from django.db.models import Model
from django.http import HttpResponse,HttpResponseNotFound,Http404,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render
from datetime import date
from .models import Post
from .forms import CommentForm

# Create your views here.

# blog_details = [
#     {
#         'slug': 'python-intro',
#         'image': 'image2.jpg',  # Add image here
#         'date': date(2026, 8, 21),
#         'title': 'Python Introduction',
#         'preview': """Python is a powerful, high-level programming language known for its simple and readable syntax.
# It is widely used in web development, data science, artificial intelligence, automation, and software development.""",
#         'content': """Python is a popular high-level programming language known for its simple and easy-to-read syntax.
# It is widely used for web development, automation, data analysis, and artificial intelligence.
# Python provides many built-in libraries and frameworks that make development faster and easier.
# It is beginner-friendly while also being powerful enough for large and complex applications.
# Because of its versatility, Python is one of the most widely used programming languages today."""
#     },
#
#     {
#         'slug': 'django-basics',
#         'image': 'image4.jpg',  # Add image here
#         'date': date(2026, 8, 22),
#         'title': 'Django Basics',
#         'preview': """Django is a powerful Python web framework used to build dynamic and scalable websites.
# It provides built-in features for handling URLs, databases, templates, forms, and user authentication.""",
#         'content': """Django is a popular Python web framework designed for developing secure and maintainable web applications.
# It follows the Model-Template-View architecture, which helps developers organize their applications efficiently.
# Django provides many built-in features such as URL routing, database management, authentication, forms, and templates.
# It also includes an administrative interface that makes managing application data much easier.
# Because of its simplicity and powerful features, Django is widely used for building modern web applications."""
#     },
#
#     {
#         'slug': 'regex',
#         'image': 'image5.jpg',  # Add image here
#         'date': date(2026, 8, 23),
#         'title': 'Regular Expressions',
#         'preview': """Regular expressions, commonly called regex, are patterns used to search, match, and manipulate text.
# They are useful for tasks such as validating input, finding specific patterns, and extracting information.""",
#         'content': """Regular expressions are sequences of characters that define a search pattern for working with text.
# They can be used to find, match, replace, and extract specific patterns from strings.
# Regex provides special characters such as ^, $, *, +, ?, and [] to create powerful search patterns.
# They are commonly used for validating email addresses, phone numbers, passwords, and other forms of input.
# Python provides the built-in re module, which makes it easy to work with regular expressions."""
#     },
#
#     {
#         'slug': 'tkinter',
#         'image': 'image6.jpg',  # Add image here
#         'date': date(2026, 8, 24),
#         'title': 'Tkinter',
#         'preview': """Tkinter is Python's standard library for creating graphical user interfaces and desktop applications.
# It provides widgets such as buttons, labels, text boxes, and menus for building interactive applications.""",
#         'content': """Tkinter is a built-in Python library used to create graphical user interfaces for desktop applications.
# It provides many widgets such as buttons, labels, entry fields, text areas, menus, and frames.
# Developers can use these widgets to create interactive applications without needing external libraries.
# Tkinter also supports event handling, allowing applications to respond to actions such as button clicks.
# Because it is simple and included with Python, Tkinter is a good choice for beginners learning GUI development."""
#     },
#]



    # {'python-intro':"python blog posts!",
    #           'django-basics':"django blog posts!",
    #           'regex':'regular expressions',
    #           'tkinter': None
    #           }

def home_page(request):
    latest_blogs=Post.objects.all().order_by('-date')[:2]
    # sorted_blogs=sorted(blog_details,key=lambda post:post['date'],reverse=True)
    # latest_blogs=sorted_blogs[:2]
    return render(request,'blogs/index.html',{'l_blogs':latest_blogs})
    # res_data=render_to_string("blogs/index.html")
    # return HttpResponse(res_data)


def blogposts(request):
    blog_details=Post.objects.all()
    # list_items=''

    return render(request,'blogs/allposts.html',{'blogs':blog_details})
    # for b in blog_list:
    #     blog_path=reverse('blog-post',args=[b])
    #     list_items+=f'<li><a href="{blog_path}">{b.capitalize()}</a></li>'
    #     res_data=f"<ul>{list_items}</ul>"
    #     return  HttpResponse(res_data)

def process_blog_name(blog):
    blog_list=blog.split("-")
    return " ".join(blog_list)

# def get_blog_by_slug(blog_url):
#     for blog in blog_details:
#         if blog['slug']==blog_url:
#             return blog
#     return None


def blog_post(request, blog):
    post_data = Post.objects.get(slug=blog)
    tags_caption = post_data.tags.all()

    if request.method=="POST":
        commented_data = request.POST
        form = CommentForm(commented_data)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post_data
            comment.save()
            return HttpResponseRedirect(reverse('blog-post',args=[blog]))
        return render(request, 'blogs/posts.html', {"post": post_data, 'tags': tags_caption, 'comment_form': form})

    # if blog=='python-intro':
    #     res = "python blog posts!"
    # elif blog=='django-basics':
    #     res = "django blog posts!"
    else:
       try:
        # res=get_blog_by_slug(blog)
        form_data=CommentForm()
        return render(request,'blogs/posts.html',{"post":post_data,'tags':tags_caption,'comment_form':form_data})
       except Exception:
        res_data=render_to_string("404.html")
        #raise Http404()



    # else:
    #     return HttpResponse(res)

# def blog_post_by_number(request, blog):
#     return HttpResponse(blog)