# urls.py
from django.urls import path
from .views import about_site

urlpatterns = [
    path('about/', about_site, name='about'),
]
