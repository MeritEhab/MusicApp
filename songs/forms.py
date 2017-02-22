from django import forms

from .models import Song


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = [
            'song_title',
             'artist',
             'genre',
             'logo',
             'audio_file',
             ]

