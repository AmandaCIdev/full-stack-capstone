from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<slug:slug>/', views.event_detail, name='event_detail'),
    path('event/create/', views.event_create, name='event_create'),
    path('event/<slug:slug>/update/', views.event_update, name='event_update'),
    path('event/<slug:slug>/delete/', views.event_delete, name='event_delete'),
    path('event/<slug:slug>/add_review/', views.add_review, name='add_review'),
    path('event/<slug:slug>/like/', views.like_event, name='like_event'),
]

