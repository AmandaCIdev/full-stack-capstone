from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Event, Reviews
from .forms import EventForm, ReviewsForm

class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.all()
    template_name = "event_list.html"
    paginate_by = 6

    # def post(self, request, *args, **kwargs):
    #     slug = self.kwargs['slug']
    #     event = get_object_or_404(Event, slug=slug)
    #     if 'like' in request.POST:
    #         event.likes.add(request.user)
    #         messages.success(request, 'Event liked successfully!')
    #     elif 'unlike' in request.POST:
    #         event.likes.remove(request.user)
    #         messages.success(request, 'Event unliked successfully!')
    #     return HttpResponseRedirect(reverse('event_detail.', args=[slug]))


class EventListView(generic.ListView):
    queryset = Event.objects.order_by('-published_on')
    print("HELLO!!")
    print(queryset)
    context_object_name = 'events'
    template_name = 'event/event_list.html'
    paginate_by = 10

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    reviews = event.reviews.all().order_by("-created_on")
    review_count = event.reviews.filter(approved=True).count()
    if request.method == "POST":
        reviews_form = ReviewsForm(data=request.POST)
        if reviews_form.is_valid():
            review = reviews_form.save(commit=False)
            review.author = request.user
            review.event = event
            review.save()
            messages.success(request, "Your review is submitted and awaiting verification")
    reviews_form = ReviewsForm()
    return render(request, "event/event_detail.html", {
        "event": event,
        "reviews": reviews,
        "review_count": review_count,
        "reviews_form": reviews_form,
    })

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
        review.save()
        messages.success(request, 'Review added successfully!')
        return redirect('event_detail', slug=slug)
    return render(request, 'event/add_review.html', {'event': event})
