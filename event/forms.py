
from django import forms
from .models import Event, Reviews

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'image', 'date', 'time', 'location', 'description', 'speaker']

class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['body',]
