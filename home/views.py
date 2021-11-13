from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

from api.models import *


def index(request):
    basic_info = BasicInfo.objects.latest('id')
    links = Link.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    context = {
        'basic_info': basic_info,
        'links': links,
        'skills': skills,
        'projects': projects
    }
    return render(request, 'pages/index.html', context)


def about(request):
    basic_info = BasicInfo.objects.latest('id')
    context = {
        'basic_info': basic_info
    }
    return render(request, 'pages/about.html', context)


def contactme(request):
    basic_info = BasicInfo.objects.latest('id')
    context = {
        'basic_info': basic_info
    }
    return render(request, 'pages/contact.html', context)


def blogs(request):
    basic_info = BasicInfo.objects.latest('id')
    blogs = Blog.objects.all()
    context = {
        'basic_info': basic_info,
        'blogs': blogs
    }
    return render(request, 'pages/blogs.html', context)


def singleBlog(request, slug):
    basic_info = BasicInfo.objects.latest('id')
    blog = get_object_or_404(Blog, slug=slug)
    context = {
        'basic_info': basic_info,
        'blog': blog
    }
    return render(request, 'pages/single-blog.html', context)
