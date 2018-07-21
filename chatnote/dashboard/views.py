from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import AddNoteForm
from .models import Note, Tag



def home(request):
    if not request.user.is_authenticated:
        print("Not authenticated")
        return return_to_login(request)

    """ Home Page """
    context = {
        'user' : request.user,
    }
    return render(request, 'dashboard/home.html', context)


@login_required
def notes(request):
    """ List all notes that the user has created
    """
    #request.user.profile.remove_friend("testbot")
    if not request.user.is_authenticated:
        return_to_login(request)
    elif request.method == 'POST':
        noteForm = AddNoteForm(data=request.POST)
        if noteForm.is_valid():
            newNote = Note.objects.create(
                user = request.user,
                description = noteForm.cleaned_data['description'],
                privacy = noteForm.cleaned_data['privacy'],
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
        print(note.user.username +"-"+ str(note.privacy))
    return render(request, 'dashboard/viewnotes.html', context)


@login_required
def profile(request, username):
    """ Displays a User's public profile
    """
    target_user = User.objects.get(username = username)
    context = {
        'user' : request.user,
        'targetuser': target_user,
        'notes' : list(Note.objects.filter(user=target_user).distinct()),
    }
    for note in context['notes']:
        note.loadTagsList()
    return render(request, 'dashboard/profile.html', context)


@login_required
def friends(request):
    #request.user.profile.add_friend(User.objects.get(username="ceri"))
    context = {
        'user':request.user,
        'friends':request.user.profile.get_friends()
    }
    return render(request, 'dashboard/friends.html', context)

def search(request):
    """ Redirect the user to input from the search bar
    """
    if request.method == 'GET':
        return redirect('/profile/' + request.GET.get('searchquery'))



def return_to_login(request):
    """ Sends user back to login screen
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return render(request, 'dashboard/home.html')
    # If request or form is invalid, returns the user to login
    form = AuthenticationForm(request)
    return render(request, 'account/login.html', {'form':form})
