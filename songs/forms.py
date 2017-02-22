from django import forms

from .models import Song
from haystack.forms import SearchForm



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





class SongArtistSearchForm(SearchForm):
    song_title = forms.CharField(required=False)
    artist = forms.CharField(required=False)

    def search(self):
        # First, store the SearchQuerySet received from other processing.
        sqs = super(SongArtistSearchForm, self).search()

        if not self.is_valid():
            return self.no_query_found()

        # Check to see if a song was chosen.
        if self.cleaned_data['song_title']:
            sqs = sqs.filter(song_title=self.cleaned_data['song_title'])

        # Check to see if an artist was chosen.
        if self.cleaned_data['artist']:
            sqs = sqs.filter(artist=self.cleaned_data['artist'])

        return sqs