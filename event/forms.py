# forms.py
from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'image', 'date', 'time', 'location', 'description', 'speaker']

        
class ReviewsForm(forms.Form):
    author = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)
