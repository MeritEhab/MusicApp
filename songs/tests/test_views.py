from django.test import TestCase
from django.contrib.auth.models import User

from songs.models import Song

class SongsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test1', email='t1@hotmail.com', password='test')
        self.user.save()

    def user_login(self):
        self.client.login(username='test1', password='test')
    
    def setUp_admin(self):
    	self.user = User.objects.create_user(username='admin', email='admin@hotmail.com', password='admin',is_superuser = True)
        self.user.save()

    def admin_login(self):
        self.client.login(username='admin', password='admin')
    
    def add_song(self, song_title="Misery", artist="Maroon 5", genre="pop"):
        return Song.objects.create(song_title=song_title, artist=artist, genre=genre)

    def test_list_songs_no_loging(self):
        action= self.client.get("/songs/")
        self.assertEqual(action.status_code, 302)

    def test_list_songs_loging(self):
    	self.user_login()
        action= self.client.get("/songs/")
        self.assertEqual(action.status_code, 200)
   

    def test_add_song_no_loging(self):
        song = self.add_song()
        action = self.client.get("/songs/add_song/")
        self.assertEqual(action.status_code, 302) 

    def test_add_song_regular_user(self):
        song = self.add_song()
        self.user_login()
        action = self.client.get("/songs/add_song/")
        #print action.status_code
        self.assertEqual(action.status_code, 302)

    def test_add_song_admin_user(self):
        song = self.add_song()
        self.admin_login()
        action = self.client.get("/songs/add_song/")
        self.assertEqual(action.status_code, 302)
        context= {                 
                  'song': song
                  }
        action = self.client.post("/songs/add_song/", context)
        self.assertEqual(action.status_code, 302)

    def test_detial_song_no_loging(self):
        song = self.add_song()
        action = self.client.get("/songs/"+str(song.id))
        self.assertEqual(action.status_code, 301) 

    def test_detail_song_user(self):
        song = self.add_song()
        self.user_login()
        action = self.client.get("/songs/" + str(song.id)+"/" )
        self.assertEqual(action.status_code, 200)
    
    def test_detail_song_admin(self):
        song = self.add_song()
        self.admin_login()
        action = self.client.get("/songs/" + str(song.id)+"/" )
        self.assertEqual(action.status_code, 302)
    
    def test_edit_song_user(self):
        song = self.add_song()
        self.user_login()
        action = self.client.get("/songs/" + str(song.id)+"/edit/" )
        self.assertEqual(action.status_code, 302)

    def test_edit_song_admin(self):
        song = self.add_song()
        self.admin_login()
        action = self.client.get("/songs/" + str(song.id)+"/edit/" )
        self.assertEqual(action.status_code, 302)
    	context= {                 
          'song': song
          }
        action = self.client.post("/songs/add_song/", context)
        self.assertEqual(action.status_code, 302)

    def test_delete_song_user(self):
        song = self.add_song()
        self.user_login()
        action = self.client.get("/songs/" + str(song.id)+"/delete/" )
        self.assertEqual(action.status_code, 302)

    def test_delete_song_admin(self):
        song = self.add_song()
        self.admin_login()
        action = self.client.get("/songs/" + str(song.id)+"/delete/" )
        self.assertEqual(action.status_code, 302)

