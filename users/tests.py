from django.test import TestCase
from django.contrib.auth.models import User

from users.models import PlayList
from songs.models import Song
from songs.models import Song

class UserTest(TestCase):

	def create_user(self, username="test1", email="t1@hotmail.com", password="test"):
		return User.objects.create_user(username=username, email=email, password=password)

	def test_registration(self):
		register = self.client.get("/accounts/signup/")
		self.assertEqual(register.status_code, 200)
		context = {
		'username': 'test',
		'email': 't@hotmail.com',
		'password1':'123456',
		'password2': '123456'
		}
		register = self.client.post("/accounts/signup/", context)
		self.assertEqual(register.status_code, 302)

	def test_login(self):
		user = self.create_user()
		user.save()
		login = self.client.get("/accounts/login/")
		self.assertEqual(login.status_code, 200)
		context = {
		'username': user.username,
		'password': user.password,
		}

		login = self.client.post("/accounts/login/", context)
		self.assertEqual(login.status_code, 200)


class PlaylistsTest(TestCase):

	def setUp(self):
		self.user = User.objects.create_user(username='test1', email='t1@hotmail.com', password='test')
		self.user.save()
	
	def user_login(self):
		self.client.login(username='test1', password='test')

	def add_song(self, song_title="Misery", artist="Maroon 5", genre="pop"):
		return Song.objects.create(song_title=song_title, artist=artist, genre=genre)
	
	def add_playlist(self, name="Playlist 1", fk_user=User.objects.get(id=1)):
	    return PlayList.objects.create(name=name, fk_user=fk_user)
	
	def test_playlist_creation(self):
		playlist = self.add_playlist()
		self.assertTrue(isinstance(playlist, PlayList))
		self.assertEqual(playlist.__str__(), playlist.name)
	
	def test_list_playlists_no_loging(self):
		action= self.client.get("/users/playlists/")
		self.assertEqual(action.status_code, 302)
	
	def test_list_songs_loging(self):
		self.user_login()
		action= self.client.get("/users/playlists/")
		self.assertEqual(action.status_code, 200)
	
	def test_add_playlist_no_loging(self):
		playlist = self.add_playlist()
		action = self.client.get("/users/add_playlist/")
		self.assertEqual(action.status_code, 302) 
	
	def test_add_playlist_user(self):
		playlist = self.add_playlist()
		self.user_login()
		action = self.client.get("/users/add_playlist/")
		self.assertEqual(action.status_code, 200)
		context= {                 
		          'playlist': playlist
		          }
		action = self.client.post("/users/add_playlist/", context)
		self.assertEqual(action.status_code, 200)

	def test_detial_playlist_no_loging(self):
		playlist = self.add_playlist()
		action = self.client.get("/users/playlists/"+str(playlist.id)+"/")
		self.assertEqual(action.status_code, 302) 

	def test_detail_palylist_user(self):
		playlist = self.add_playlist()
		self.user_login()
		action = self.client.get("/users/playlists/" + str(playlist.id)+"/" )
		self.assertEqual(action.status_code, 200)
	
	def test_edit_playlist_no_loging(self):
		playlist = self.add_playlist()
		action = self.client.get("/users/playlists/" + str(playlist.id)+"/edit/")
		self.assertEqual(action.status_code, 302) 

	def test_edit_playlist_user(self):
		playlist = self.add_playlist()
		self.user_login()
		action = self.client.get("/users/playlists/" + str(playlist.id)+"/edit/" )
		self.assertEqual(action.status_code, 200)
		context= {                 
		  'playlist': playlist
		  }
		action = self.client.post("/users/playlists/" + str(playlist.id)+"/edit/", context)
		self.assertEqual(action.status_code, 200)

	def test_delete_playlist_user(self):
		playlist = self.add_playlist()
		self.user_login()
		action = self.client.post("/users/playlists/" + str(playlist.id)+"/delete/" )
		self.assertEqual(action.status_code, 302)

	def test_add_song_to_playlist_user(self):
		playlist = self.add_playlist()
		song = self.add_song()
		self.user_login()
		action = self.client.get("/songs/"+str(song.id)+"/")
		playlist.songs.add(song)
		self.assertEqual(action.status_code, 200)