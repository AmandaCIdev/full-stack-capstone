from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import About
from .forms import SubmitDetailsForm

def about_site(request):
    
    about = About.objects.order_by('updated_on').first()

    if request.method == "POST":
        print("Received a POST request")
        submit_details_form = SubmitDetailsForm(data=request.POST)
        if submit_details_form.is_valid():
            submit_details_form.save()
            messages.add_message(request, messages.SUCCESS, "Your details have been received! I endeavor to respond within 2 working days.")
    
    submit_details_form = SubmitDetailsForm()

    print("About to render template")

    return render(
        request,
        "about/about.html",
        {'about': about, "submit_details_form": submit_details_form},

    )



