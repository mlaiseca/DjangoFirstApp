from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Mario',
        'title': 'Blog post 1',
        'content': 'first post content',
        'date_posted': 'April 28, 2020'
    },
    {
        'author': 'Joe',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': 'April 28, 2020'
    }
]


def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
