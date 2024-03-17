from django.urls import path
from . import views

app_name = 'about'  # Example namespace for the 'about' app

urlpatterns = [
    path('', views.about_site, name='about'),  # URL pattern
]



