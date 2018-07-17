from django import forms
from .models import Note, Tag

class AddNoteForm(forms.ModelForm):
    tags = forms.CharField(max_length=25)
    class Meta:
        model = Note
        fields = ('tags', 'description', )

class SearchForm(forms.Form):
    query = forms.CharField(max_length=30)
    class Meta:
        fields = ('query',)
