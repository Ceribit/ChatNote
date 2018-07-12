from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm
from .models import Profile

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
    return render(request, 'registration/signup.html', context)


def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Changed my views.py'
    user.save()

def register_profile(profile, profile_form):
    profile.first_name = profile_form.cleaned_data['first_name']
    profile.last_name = profile_form.cleaned_data['last_name']
    profile.email = profile_form.cleaned_data['email']
    profile.birth_date = profile_form.cleaned_data['birth_date']

    profile.save()
