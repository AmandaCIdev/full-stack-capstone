from django.contrib import admin, messages
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
from cloudinary.models import CloudinaryField

class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_posts", null=True)
    content = models.TextField(null=True)
    published_on = models.DateTimeField(auto_now_add=True, null=True)
    image = CloudinaryField('image', blank=True)
    date = models.DateField(default=timezone.now) 
    time = models.TimeField(default=timezone.now)  
    location = models.CharField(max_length=100, default="Default location")  
    description = models.TextField(default="Default description")  
    speaker = models.CharField(max_length=100, null=True)  
    likes = models.ManyToManyField(User, related_name='liked_events', blank=True)
    front_image = CloudinaryField('image', blank=True)
    back_content = models.TextField(default="Date: {date}\nTime: {time}\nLocation: {location}\nDescription: {description}\nSpeaker: {speaker}")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

class Reviews(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_reviews") 
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review | {self.body} | by {self.author}"

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'time', 'location']
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        messages.success(request, 'Event saved successfully!')

