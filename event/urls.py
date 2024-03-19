from django.urls import path
from . import views


urlpatterns = [
    path('', views.EventList.as_view(), name='home'),  # List and home of all event flip cards
    path('<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),  # Event detail view 
    path('create/', views.event_create, name='create'),  # Create a new event
    path('<slug:slug>/update/', views.event_update, name='update'),  # Update an event
    path('<slug:slug>/delete/', views.event_delete, name='delete'),  # Delete an event
    path('<slug:slug>/add_review/', views.add_review, name='add_review'),  # Add a review to an event
    path('<slug:slug>/attend/', views.attend_event, name='attend_event'),  # Attend an event
]


