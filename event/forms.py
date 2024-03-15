# forms.py
from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'image', 'date', 'time', 'location', 'description', 'speaker']