from django.shortcuts import render
from pysondb import db
import os

# from templates import base.html
# from templates.homepage import blogs.html, contact.html, experience.html, projects.html, skills.html

# Create your views here.


def HomePageView(request):
    homepage_data = db.getDb('database/homepage.json')

    MyName = os.getenv('MY_NAME', 'My Name')
    MyProfession = os.getenv('MY_PROFESSION', 'MyProfession')
    MyCollege = os.getenv('MY_COLLEGE', 'MyCollege')

    try:
        homepage_data.add(
            {"name": MyName, "profession": MyProfession, "college": MyCollege})
    except:
        print('Data not added')
git branch -M main
    # homepage_data_list = homepage_data.getAll()
    homepage_data_list = []
    print(homepage_data_list)
    context = {'homepage_data_list': homepage_data_list}
    return render(request, 'homepage/base.html', context)


def BlogsPageView(request):
    context = {}
    return render(request, 'homepage/blogs.html', context)


def ContactPageView(request):
    context = {}
    return render(request, 'homepage/contact.html', context)
