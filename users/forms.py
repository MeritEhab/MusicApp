from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms

from .models import PlayList

        
class PlaylistForm(forms.ModelForm):
    class Meta:
        model = PlayList
        fields = [
            'name',
            ]