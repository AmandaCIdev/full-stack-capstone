from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About
from .forms import SubmitDetailsForm

def about_site(request):
    # Fetch the latest About information
    about = About.objects.order_by('updated_on').first()
    
    # Instantiate the SubmitDetailsForm
    submit_details_form = SubmitDetailsForm()
    
    if request.method == "POST":
        # If the request method is POST, process form submission
        submit_details_form = SubmitDetailsForm(data=request.POST)
        if submit_details_form.is_valid():
            # If form is valid, save form data
            submit_details_form.save()
            # Display success message
            messages.success(request, "Your details have been received! I endeavor to respond within 2 working days.")
            # Redirect to prevent form resubmission when refreshing the page
            return redirect('about')
    
    # Render the about page template with about details and form
    return render(
        request,
        "about/about.html",
        {'about': about, "submit_details_form": submit_details_form},
    )

def about(request):
    # Process the form submission for the about page
    if request.method == 'POST':
        form = SubmitDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or render a success message
            return redirect('success_page')  # Replace 'success_page' with the name of your success URL
    else:
        # If request method is GET, display the form
        form = SubmitDetailsForm()
    return render(request, 'about.html', {'form': form})
