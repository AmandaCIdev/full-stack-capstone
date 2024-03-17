# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About
from .forms import SubmitDetailsForm

def about_site(request):
    about = About.objects.order_by('updated_on').first()
    submit_details_form = SubmitDetailsForm()

    if request.method == "POST":
        submit_details_form = SubmitDetailsForm(data=request.POST)
        if submit_details_form.is_valid():
            submit_details_form.save()
            messages.success(request, "Your details have been received! I endeavor to respond within 2 working days.")
            return redirect('about')
    
    return render(
        request,
        "about/about.html",
        {'about': about, "submit_details_form": submit_details_form},
    )

def about(request):
    if request.method == 'POST':
        form = SubmitDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = SubmitDetailsForm()
    return render(request, 'about.html', {'form': form})
