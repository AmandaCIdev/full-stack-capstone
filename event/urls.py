from django.urls import path
from . import views

""" REORDER urlpatterns """

urlpatterns = [
    path('create/', views.event_create, name='create'),  # Create a new event
    path('<slug:slug>/update/', views.event_update, name='update'),  # Update an event
    path('<slug:slug>/delete/', views.event_delete, name='delete'),  # Delete an event
    path('<slug:slug>/edit_review/<int:review_id>', views.review_edit, name='review_edit'), # Edit an event review
    path('<slug:slug>/delete_review/<int:review_id>', views.review_delete, name='review_delete'), # Delete an event review
    path('<slug:slug>/add_review/', views.add_review, name='add_review'),  # Add a review to an event
    path('<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),  # Event detail view 
    path('', views.EventList.as_view(), name='home'),  # Event List and Home of flip cards
    path('like/<slug:slug>', views.LikeView, name='like_post'), # Endpoint for liking a post
]
