from django.urls import path
from . import views

""" REORDER urlpatterns """

urlpatterns = [
    path('create/', views.event_create, name='create'),  
    path('<slug:slug>/update/', views.event_update, name='update'), 
    path('<slug:slug>/delete/', views.event_delete, name='delete'),  
    path('<slug:slug>/edit_review/<int:review_id>', views.review_edit, name='review_edit'), 
    path('<slug:slug>/delete_review/<int:review_id>', views.review_delete, name='review_delete'), 
    path('<slug:slug>/add_review/', views.add_review, name='add_review'),  
    path('<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),  
    path('', views.EventList.as_view(), name='home'),  
    path('like/<slug:slug>', views.LikeView, name='like_post'), 
]
