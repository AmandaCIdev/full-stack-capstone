from .models import SubmitDetails
from django import forms


class SubmitDetailsForm(forms.ModelForm):

    class Meta:

        model = SubmitDetails

        fields = ("name", "email", "message", "phone_number")