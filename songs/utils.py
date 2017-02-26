import json
import requests

from songs.models import Song

def save_song():

    song = Song(
        song_title="Song1",
        artist="A1",
        genre="pop",
    )
    song.save()