"""
Views.py
"""
# pylint: disable=locally-disabled, no-member
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import Event, Reviews
from .forms import EventForm, ReviewsForm
from django.http import JsonResponse



def LikeView(request, slug):
    event = get_object_or_404(Event, slug=slug)

    user_like = False

    if event.likes.filter(id=request.user.id).exists():
        event.likes.remove(request.user)
        user_like = False
    else:
        event.likes.add(request.user)
        user_like = True

    return HttpResponseRedirect(reverse('event_detail', args=[slug]))


class EventList(ListView):

    class EventList(ListView):
        """Home page view for displaying events"""

    model = Event
    template_name = 'event_list.html'  # Specify the template name
    context_object_name = 'event_list'  # Specify the context object name
    paginate_by = 6  # Specify the number of items per page

    def get_queryset(self):
        """Return the queryset of events."""
        return Event.objects.all()

        
class EventDetail(View):
    """Event details page"""

    def get(self, request, slug):
        queryset = Event.objects.filter(slug=slug)
        event = get_object_or_404(queryset, slug=slug)
        likes = event.likes.count()
        reviews = event.reviews.all().order_by("-created_on")
        review_count = event.reviews.filter(approved=True).count()
        reviews_form = ReviewsForm()  # Define the form initially

        user_like = False
        if event.likes.filter(id=request.user.id).exists():
            user_like = True


        if request.method == "POST":
            print("Received a POST request")
            reviews_form = ReviewsForm(data=request.POST)
            if reviews_form.is_valid():
                review = reviews_form.save(commit=False)
                review.author = request.user
                review.event = event
                review.save()
                messages.add_message(request, messages.SUCCESS, "Your review is submitted and awaiting verification")

                
                reviews_form = ReviewsForm() # Reset the form after successful submission

        return render(request, "event/event_detail.html", {"event": event, "reviews": reviews,
                                                           "review_count": review_count, "reviews_form": reviews_form,
                                                           "likes": likes, "user_like": user_like, })

def review_edit(request, slug, review_id):
        """View to edit comments."""
        if request.method == "POST":
            queryset = Event.objects.all()
            event = get_object_or_404(queryset, slug=slug)
            review = get_object_or_404(Reviews, pk=review_id)
            review_form = ReviewsForm(data=request.POST, instance=review)

            if review_form.is_valid() and review.author == request.user:
                review = review_form.save(commit=False)
                review.event = event
                review.approved = False
                review.save()
                messages.add_message(request, messages.SUCCESS, 'Review Updated!')
            else:
                messages.add_message(request, messages.ERROR, 'Error updating review!')

            return HttpResponseRedirect(reverse('event_detail', args=[slug]))


def review_delete(request, slug, review_id):
    """View to delete review."""
    queryset = Event.objects.all()
    event = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Reviews, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('event_detail', args=[slug]))



def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event created successfully!')
            return redirect('event_list')
        else:
            messages.error(request, 'Failed to create event. Please correct the errors.')
    else:
        form = EventForm()
    return render(request, 'event/event_form.html', {'form': form})


def event_update(request, slug):
    event = get_object_or_404(Event, slug=slug)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('event_list')
        else:
            messages.error(request, 'Failed to update event. Please correct the errors.')
    else:
        form = EventForm(instance=event)
    return render(request, 'event/event_form.html', {'form': form})


def event_delete(request, slug):
    event = get_object_or_404(Event, slug=slug)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect('event_list')
    return render(request, 'event/event_confirm_delete.html', {'event': event})


def add_review(request, slug):
    event = get_object_or_404(Event, slug=slug)
    if request.method == 'POST':
        body = request.POST.get('body')
        author = request.user
        review = Reviews.objects.create(event=event, author=author, body=body)
        reviews = event.reviews.all().order_by("-created_on").filter(approved=True) # filter reviews to show only the one is approved
        review.save()
        messages.success(request, 'Review added successfully!')
        return redirect('event_detail', slug=slug)
    return render(request, 'event/add_review.html', {'event': event})


