from .models import SubmitDetails
from django import forms


class SubmitDetailsForm(forms.ModelForm):
    class Meta:
        model = SubmitDetails
        fields = ("name", "email", "message", "phone_number")

    # You can add additional form fields or customize existing ones here
    # For example, if you want to add a subject field:
    subject = forms.CharField(max_length=100, required=True, label="Subject")

    # If you want to customize the labels or placeholders of existing fields:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Your Name"
        self.fields['email'].label = "Your Email Address"
        self.fields['message'].label = "Your Message"
        self.fields['phone_number'].label = "Your Phone Number"

    # If you want to add custom validation logic:
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        # Add your custom validation logic here
        return phone_number
