from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length = 24, required=False,
                                help_text='Optional.')
    last_name = forms.CharField(max_length = 24, required=False,
                                help_text='Optional.')
    email = forms.EmailField(max_length = 254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
        'password1', 'password2', )


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'birth_date')


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'birth_date')
    def __init__(self, *args, **kwargs):
        super(SettingsForm, self).__init__(*args, **kwargs)
        self.fields['last_name'].required = False
        self.fields['first_name'].required = False
        self.fields['email'].required = False
        self.fields['birth_date'].required = False

class DescriptionForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('description',)
