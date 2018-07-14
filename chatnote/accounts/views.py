from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm, SettingsForm, DescriptionForm
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
    return render(request, 'account/signup.html', context)


def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Changed my views.py'
    user.save()


@login_required
def settings(request):
    if request.method == 'POST':
        profile = request.user.profile
        profile_form = SettingsForm(request.POST)
        description_form = DescriptionForm(request.POST, instance = request.user.profile)
        if profile_form.is_valid():
            ProfileSave(profile_form, profile)
        if description_form.is_valid():
            description_form.save()
            print('description changed')
        else:
            print('jk')
        return redirect('/settings')
    context = {
        'user':request.user,
        'profile_form':SettingsForm(),
        'description_form' : DescriptionForm()
    }
    return render(request, 'account/settings.html', context)


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
