from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contactme/', contactme, name='contactme'),
    path('blogs/<slug:slug>/', singleBlog, name='single-blog'),
    path('blogs/', blogs, name='blogs'),
]
