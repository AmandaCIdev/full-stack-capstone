from django.urls import path
from . import views

app_name = 'event'  # Namespace for the event app

urlpatterns = [
    path('', views.EventList.as_view(), name='event_list'),  # List of all events
    path('event/<slug:slug>/', views.event_detail, name='event_detail'),  # Event detail view
    path('event/create/', views.event_create, name='event_create'),  # Create a new event
    path('event/<slug:slug>/update/', views.event_update, name='event_update'),  # Update an event
    path('event/<slug:slug>/delete/', views.event_delete, name='event_delete'),  # Delete an event
    path('event/<slug:slug>/add_review/', views.add_review, name='add_review'),  # Add a review to an event
]
