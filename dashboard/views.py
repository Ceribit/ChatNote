from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render

def home(request):
    #if not logged in
    if not request.user.is_authenticated:
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
        return render(request, 'dashboard/home.html')
    #if not logged in

def move_home(request):
    form = AuthenticationForm(request)
    return render(request, 'registration/login.html', {'form':form})
