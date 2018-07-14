from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def home(request):
    #if not logged in
    if not request.user.is_authenticated:
        print('YOU DID NOT LOG IN')
        form = AuthenticationForm()
        if request.method == 'GET':
            return move_home(request)

        elif request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                login(request, form.get_user())
                return render(request, 'dashboard/home.html')
        return move_home(request)
    else:
        print('You are logged in')
        context = {
            'user' : request.user
        }
        print('You are' + context['user'].profile.first_name)
        return render(request, 'dashboard/home.html', context)
    #if not logged in

def move_home(request):
    form = AuthenticationForm(request)
    return render(request, 'account/login.html', {'form':form})
