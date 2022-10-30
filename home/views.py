from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

from api.models import *


def index(request, flag=False):
    basic_info = BasicInfo.objects.latest('id')
    links = Link.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    resume = Link.objects.filter(name='Resume').first()

    context = {
        'basic_info': basic_info,
        'links': links,
        'resume': resume,
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


def basicInfo(request, flag=False):
    result = {}
    basicInfo = BasicInfo.objects.all()

    for info in basicInfo:
        result[info.id] = {
            'name': info.name,
            'place': info.place,
            'caption_tags': info.caption_tags,
            'description': info.description,
            'about_title': info.about_title,
            'about_description': info.about_description,
            'profile_image_url': info.profile_image_url
        }

    if flag:
        return result

    return JsonResponse(result)


def projects(request, flag=False):
    result = {}
    projects = Project.objects.all()

    for project in projects:
        result[project.id] = {
            'title': project.title,
            'description': project.description,
            'image': project.image_url,
            'url': project.url,
            'tech_stack': project.tech_stack
        }

    if flag:
        return result

    return JsonResponse(result)


def experience(request, flag=False):
    result = {}
    experiences = Experience.objects.all()

    for experience in experiences:
        result[experience.id] = {
            'company_name': experience.company_name,
            'position': experience.position,
            'start_date': experience.start_date,
            'end_date': experience.end_date,
            'tech_stack': experience.tech_stack,
            'description': experience.description
        }

    if flag:
        return result

    return JsonResponse(result)


def education(request, flag=False):
    result = {}
    educations = Education.objects.all()

    for education in educations:
        result[education.id] = {
            'school_name': education.school_name,
            'degree': education.degree,
            'start_date': education.start_date,
            'end_date': education.end_date,
            'field_of_study': education.field_of_study,
            'description': education.description
        }

    if flag:
        return result

    return JsonResponse(result)


def skills(request, flag=False):
    result = {}
    skills = Skill.objects.all()

    for skill in skills:
        result[skill.id] = {
            'name': skill.name,
            'priority': skill.priority,
            'description': skill.description
        }

    if flag:
        return result

    return JsonResponse(result)


def links(request, flag=False):
    result = {}
    links = Link.objects.all()

    for link in links:
        result[link.name] = {
            'name': link.name,
            'url': link.url,
            'icon_url': link.icon_url
        }

    if flag:
        return result

    return JsonResponse(result)


def tags(request, flag=False):
    result = {}
    tags = Tag.objects.all()

    for tag in tags:
        result[tag.id] = {
            'name': tag.name
        }

    if flag:
        return result

    return JsonResponse(result)


def allAPIData(request, flag=False):
    result = {
        'basic_info': basicInfo(request, True),
        'projects': projects(request, True),
        'experience': experience(request, True),
        'education': education(request, True),
        'skills': skills(request, True),
        'links': links(request, True),
        'Tags': tags(request, True),
    }
    return JsonResponse(result)
