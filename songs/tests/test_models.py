from django.test import TestCase

from songs.models import Song

class SongsTest(TestCase):
	
    def add_song(self, song_title="Misery", artist="Maroon 5", genre="pop"):
        return Song.objects.create(song_title=song_title, artist=artist, genre=genre)

    def test_song_creation(self):
        song = self.add_song()
        self.assertTrue(isinstance(song, Song))
        self.assertEqual(song.__str__(), song.artist+'-'+song.song_title)