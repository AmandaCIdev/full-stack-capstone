from django.contrib import admin, messages
from .models import Event, Reviews

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'time', 'location']
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        messages.success(request, 'Event saved successfully!')

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['event', 'author', 'created_on', 'approved']
    list_filter = ['approved']
    search_fields = ['event__title', 'author__username', 'body']
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        messages.success(request, 'Review saved successfully!')

# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(Reviews, ReviewsAdmin)
