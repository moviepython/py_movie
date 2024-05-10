from django import forms
from .models import List_Movies


class Movie_form(forms.ModelForm):
    class Meta:
        model = List_Movies
        fields = ['movies', 'year', 'desc', 'f_name', 'm_name', 'link']


