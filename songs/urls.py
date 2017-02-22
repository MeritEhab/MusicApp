from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from songs.views import(
	ListSongs, DetailSongs, 
	CreateSong, UpdateSong, DeleteSong
	)

app_name = 'song'
urlpatterns = [
    url(r'^$', login_required(ListSongs.as_view()), name ='show_songs'),
    url(r'^(?P<pk>[0-9]+)/$',login_required(DetailSongs.as_view()),name='song_detial'),
    url(r'^add_song/$',login_required(CreateSong.as_view()),name='add_song'),
    url(r'^(?P<pk>\d+)/edit/$',login_required(UpdateSong.as_view()),name='song_edit'),
    url(r'^(?P<pk>\d+)/delete/$',login_required(DeleteSong.as_view()),name='song_delete'),
]