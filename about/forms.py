from .models import SubmitDetails
from django import forms


class SubmitDetailsForm(forms.ModelForm):
    class Meta:
        model = SubmitDetails
        fields = ("name", "email", "message", "phone_number")

    
    subject = forms.CharField(max_length=100, required=True, label="Subject")

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Your Name"
        self.fields['email'].label = "Your Email Address"
        self.fields['message'].label = "Your Message"
        self.fields['phone_number'].label = "Your Phone Number"

   
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        
        return phone_number
