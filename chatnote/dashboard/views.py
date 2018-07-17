from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import AddNoteForm
from .models import Note, Tag
def home(request):
    #if not logged in
    if not request.user.is_authenticated:
        return_to_login(request)
    elif request.method == 'POST':
        noteForm = AddNoteForm(data=request.POST)
        if noteForm.is_valid():
            newNote = Note.objects.create(
                user = request.user,
                description = noteForm.cleaned_data['description'],
            )
            for splitTag in noteForm.cleaned_data['tags'].split():

                if not Tag.objects.filter(word = splitTag.lower()).exists():
                    tag = Tag(word = splitTag.lower())
                    tag.save()
                else:
                    tag = Tag.objects.get(word=splitTag.lower())
                newNote.tags.add(tag)
            newNote.save()
        else:
            print(noteForm.errors)
    context = {
        'user' : request.user,
        'noteForm' : AddNoteForm(),
        'notes' : list(Note.objects.filter(user=request.user).distinct())
    }
    for note in context['notes']:
        note.loadTagsList()
    return render(request, 'dashboard/home.html', context)

def profile(request, username):
    context = {
        'user':request.user,
        'targetuser':User.objects.get(username = username),
    }
    return render(request, 'dashboard/profile.html', context)

def search(request):
    if request.method == 'GET':
        return redirect('/profile/' + request.GET.get('searchquery'))


def move_home(request):
    form = AuthenticationForm(request)
    return render(request, 'account/login.html', {'form':form})

def return_to_login(request):
    form = AuthenticationForm()
    if request.method == 'GET':
        return move_home(request)

    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return render(request, 'dashboard/home.html')
    return move_home(request)
