from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from .models import User
from events.models import Event, EventRegistration
# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            messages.success(request, f'Your account has been created! You are now able to log in')
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})

@login_required
def profile(request):
    user_events_id = [x for x in EventRegistration.objects.filter(user=request.user.email).values_list('event_id', flat=True)]
    user_events = Event.objects.filter(event_id__in=user_events_id)
    
    context = {"user_events": user_events}
    return render(request, 'users/profile.html', context=context)

@login_required
def del_user(request):
    if request.method == "GET":
        return render(request, 'users/confirm_del.html')
    else:
        user = User.objects.get(email=request.user.email)
        user.delete()
        return redirect('blogs-index')
    
@login_required
def edit_user(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'users/update_profile.html', context)

# @login_required
# def test(request):
#     events = Event.objects.all()
#     context = {'events':events}
#     return render(request, 'users/test.html', context)