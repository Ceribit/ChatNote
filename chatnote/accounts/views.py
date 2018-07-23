from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.db import models
from .forms import UserForm, ProfileForm, SettingsForm, DescriptionForm
from .models import Profile, Notification

def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = Profile.objects.get(user = user)
            register_profile(profile, profile_form)
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            print('Account created')
            return redirect('/')
        else:
            print('Forms were not valid')
    context = {
        'user_form': UserForm(),
        'profile_form': ProfileForm()
    }
    print('METHOD WAS NOT POST')
    return render(request, 'account/signup.html', context)


@login_required
def complete_request(request, id):
    if request.method == 'POST':
        if request.POST.get('response_type') == 'Accept':
            from_user = User.objects.get(id=id)
            notification = Notification.objects.get(from_user=from_user)
            if(notification.target_user == request.user):
                notification.delete()
                request.user.profile.add_friend(from_user)
        else:
            from_user = User.objects.get(id=id)
            notification = Notification.objects.get(from_user=from_user)
            if(notification.target_user == request.user):
                notification.delete()
    return redirect('/notifications')


@login_required
def send_request(request, id):
    if User.objects.filter(id = id).exists():
        target_user = User.objects.get(id=id)
        request.user.profile.send_friend_request(
            target_user=target_user,
            message="N/A",
            type = 2)
        print('Request sent')
    else:
        print("ID does not exist")

    return redirect('/friends')

@login_required
def remove_friend(request, id):
    if User.objects.filter(id = id).exists():
        target_user = User.objects.get(id=id)
        request.user.profile.remove_friend(target_user)
        print('Friend removed')
    else:
        print("Friend not removed")

    return redirect('/profile/' +  target_user.username)


@login_required
def settings(request):
    if request.method == 'POST':
        profile = request.user.profile
        profile_form = SettingsForm(request.POST)
        description_form = DescriptionForm(request.POST, instance = request.user.profile)
        if profile_form.is_valid():
            ProfileSave(profile_form, profile)
        if description_form.is_valid():
            DescriptionSave(description_form, profile)
        return redirect('/settings')
    context = {
        'user':request.user,
        'profile_form':SettingsForm(),
        'description_form' : DescriptionForm()
    }
    return render(request, 'account/settings.html', context)

@login_required
def notifications(request):
    notifications_list = Notification.objects.filter(target_user = request.user)
    context = {
    'user' : request.user,
    'notifications' : notifications_list
    }
    print(notifications_list)
    return render(request, 'account/notifications.html', context)


def register_profile(profile, profile_form):
    profile.first_name = profile_form.cleaned_data['first_name']
    profile.last_name = profile_form.cleaned_data['last_name']
    profile.email = profile_form.cleaned_data['email']
    profile.birth_date = profile_form.cleaned_data['birth_date']
    profile.save()


def ProfileSave(form, profile):
    if str(form.cleaned_data['first_name']):  profile.first_name = form.cleaned_data['first_name']
    if str(form.cleaned_data['last_name']): profile.last_name = form.cleaned_data['last_name']
    if str(form.cleaned_data['email']): profile.email = form.cleaned_data['email']
    if not str(form.cleaned_data['birth_date']) == 'None': profile.birth_date = form.cleaned_data['birth_date']
    profile.save()


def DescriptionSave(form , profile):
    if not form.cleaned_data.get('description'):
        print('Exception found')
        return False
    form.save()
    return form
