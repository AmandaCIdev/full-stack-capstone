from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Event, Reviews
from .forms import EventForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event/event_list.html', {'events': events})

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'event/event_detail.html', {'event': event})

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

def like_event(request, slug):
    event = get_object_or_404(Event, slug=slug)
    if request.method == 'POST':
        # Toggle like status for the current user
        if request.user in event.likes.all():
            event.likes.remove(request.user)
            messages.success(request, 'Event unliked successfully!')
        else:
            event.likes.add(request.user)
            messages.success(request, 'Event liked successfully!')
    return redirect('event_detail', slug=slug)

