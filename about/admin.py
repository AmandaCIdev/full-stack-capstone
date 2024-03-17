from django.contrib import admin
from .models import About, SubmitDetails
from django_summernote.admin import SummernoteModelAdmin

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('message',)

@admin.register(SubmitDetails)
class SubmitDetailsAdmin(admin.ModelAdmin):
    list_display = ('message', 'name', 'email', 'phone_number', 'read',)
