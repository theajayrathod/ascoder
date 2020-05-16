from django.shortcuts import render, HttpResponse
from blog.models import *

# Create your views here.
def blogHome(request):
    allPost = Post.objects.all()
    print(allPost)
    return render(request, "blog/blogHome.html")


def blogPost(request, slug):
    return render(request, "blog/blogPost.html")

