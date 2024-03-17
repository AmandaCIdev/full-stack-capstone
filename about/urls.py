from django.urls import path

app_name = 'about'  # Example namespace for the 'about' app

urlpatterns = [
    path('', views.about_site, name='about'),  # URL pattern
]
