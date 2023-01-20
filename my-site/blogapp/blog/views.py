from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import Blog,Category



def index (request):
    if not request.user.is_authenticated:
        return redirect("login")
    data = {
    "Blogs": Blog.objects.filter(is_active=True,is_home=True),
    "Categories": Category.objects.all()
}

    return render(request,"blog/index.html",data)

def blogs (request):
    if not request.user.is_authenticated:
        return redirect("login")
    data = {
    "Blogs": Blog.objects.filter(is_active=True),
    "Categories": Category.objects.all()
}
    return render(request,"blog/blogs.html",data)

def blog_details (request,slug):
    if not request.user.is_authenticated:
        return redirect("login")
    data= {
        "blog": Blog.objects.get(slug=slug),
    }
    return render(request,"blog/blog-details.html",data)


def blog_by_category (request,slug):
  data = {
    "Blogs": Category.objects.get(slug=slug).blog_set.all(),
    "Categories": Category.objects.all(),
    "selected_category": slug
  }
  return render(request,"blog/blogs.html",data)