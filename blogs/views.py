from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return render(request, 'blogs/index.html')

def about(request):
    context = {}
    return render(request, 'blogs/about.html', context)

def gallery(request):
    return render(request, 'blogs/gallery.html')

def fests(request):
    return render(request, 'blogs/fests.html')

def fest(request, id):
    return redirect("events-event", id=id)

def com_mem(request):
    return render(request, 'blogs/com_mem.html')