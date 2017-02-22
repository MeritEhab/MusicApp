from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from users.views import (
	ListPlaylists, DetailPlaylist,
	CreatePlaylist, UpdatePlaylist, DeletePlaylist
	)

app_name = 'user'

urlpatterns = [

    url(r'^add_playlist/$', login_required(CreatePlaylist.as_view()), name='create-playlist'),
    url(r'^playlists/$', login_required(ListPlaylists.as_view()), name='playlist_list'),
    url(r'^playlists/(?P<pk>\d+)/$',login_required(DetailPlaylist.as_view()),name='playlist_details'),
    url(r'^playlists/(?P<pk>\d+)/edit/$',login_required(UpdatePlaylist.as_view()),name='playlist_edit'),
    url(r'^playlists/(?P<pk>\d+)/delete/$',login_required(DeletePlaylist.as_view()),name='playlist_delete'),

]