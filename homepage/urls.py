from django.urls import path
from homepage.views import HomePageView, BlogsPageView, ContactPageView

urlpatterns = [
    path('', HomePageView, name='home'),
    path('blogs/', BlogsPageView, name='blogs'),
    path('contact/', ContactPageView, name='contact')
]
