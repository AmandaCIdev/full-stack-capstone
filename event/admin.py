from django.contrib import admin, messages
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'time', 'location']
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        messages.success(request, 'Event saved successfully!')

# Register your models here.
admin.site.register(Event, EventAdmin)
