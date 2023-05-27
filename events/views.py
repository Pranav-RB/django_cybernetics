import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, EventRegistration
from users.models import User

def events_home(request):
    events = Event.objects.all()
    user_events,user_event_list = {}, {}
    if request.user.is_authenticated:
        user_events = EventRegistration.objects.filter(user=request.user.email)
        user_event_list = [x.event_id for x in user_events]
    context = {"events": events, "user_events": user_events,"user_event_list":user_event_list}
    return render(request, "events/home.html", context)

def fest_events(request, id):
    events = Event.objects.filter(fest=id)
    user_events,user_event_list = {}, {}
    if request.user.is_authenticated:
        user_events = EventRegistration.objects.filter(user=request.user.email)
        user_event_list = [x.event_id for x in user_events]
    context = {"events": events, "user_events": user_events,"user_event_list":user_event_list}
    return render(request, "events/home.html", context)

def events_test(request):
    user_events_id = [x for x in EventRegistration.objects.filter(user=request.user.email).values_list('event_id', flat=True)]
    user_events = Event.objects.filter(event_id__in=user_events_id)
    context = {"user_events": user_events}
    return render(request, "events/test.html", context)

@login_required
def events_register(request,pk):
    event = Event.objects.get(event_id=pk)
    user = User.objects.get(email=request.user.email)
    if event.event_attendees < event.event_attendees_limit:
        event.event_attendees_list += request.user.email + "\n"
        user.events_list += event.event_name + "\n"
        event.event_attendees += 1
        event.save()
        user.save()
        EventRegistration.objects.create(event_id=event, user=request.user)
        return redirect('events-home')

@login_required
def events_unregister(request,pk):
    event = Event.objects.get(event_id=pk)
    user = User.objects.get(email=request.user.email)
    user.events_list = user.events_list.replace(event.event_name + "\n",'')
    event.event_attendees_list = event.event_attendees_list.replace(request.user.email + "\n", "")
    event.event_attendees -= 1
    event.save()
    user.save()
    EventRegistration.objects.filter(event_id=event, user=request.user).delete()
    return redirect('profile')

def single_event(request, pk):
    user_events,user_event_list = {}, {}
    if request.user.is_authenticated:
        user_events = EventRegistration.objects.filter(user=request.user.email)
        user_event_list = [x.event_id for x in user_events]
    event = Event.objects.get(event_id=pk)
    rules = event.rules.split("\n")
    prereqs = [x for x in event.prereq.split("\n") if x != '']
    seats_left = event.event_attendees_limit - event.event_attendees
    context = {"event": event, "rules": rules, "prereqs": prereqs,"user_event_list":user_event_list,"seats_left":seats_left}
    return render(request, "events/single_event.html", context)