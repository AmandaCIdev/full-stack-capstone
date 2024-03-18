from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventList.as_view(), name='home'),  # List of all events
    path('<slug:slug>/', views.event_detail, name='detail'),  # Event detail view 
    path('create/', views.event_create, name='create'),  # Create a new event
    path('<slug:slug>/update/', views.event_update, name='update'),  # Update an event
    path('<slug:slug>/delete/', views.event_delete, name='delete'),  # Delete an event
    path('<slug:slug>/add_review/', views.add_review, name='add_review'),  # Add a review to an event
]
