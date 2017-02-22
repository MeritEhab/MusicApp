from django.test import TestCase
from django.contrib.auth.models import User

from users.models import PlayList

class PlaylistsTest(TestCase):
	
	def add_playlist(self, name="Playlist 1", fk_user=User.objects.get(id=1)):
	    return PlayList.objects.create(name=name, fk_user=fk_user)
	
	def test_playlist_creation(self):
		playlist = self.add_playlist()
		self.assertTrue(isinstance(playlist, PlayList))
		self.assertEqual(playlist.__str__(), playlist.name)