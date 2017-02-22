from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView, View
    )
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import SongForm
from .models import Song
from users.models import PlayList

class ListSongs(ListView):
    model = Song
    template_name ="songs/list_songs.html"

class DetailSongs(View):
    template_name ="songs/detail.html"

    def get(self,request,pk):
        song = get_object_or_404(Song, id=pk)

        playlists = PlayList.objects.filter(fk_user=request.user)
        context ={
            'song':song,
            'playlist':playlists,
            }
        return render(request,'songs/detail.html',context)

    def post(self, request, pk):
        song = Song.objects.get(id=pk)
        print request.POST.get('playlist_select') 

        if request.POST.get('playlist_select'):
            playlistID = request.POST.get('playlist_select')
            playlist_obj = PlayList.objects.get(id=playlistID)
            playlist_obj.songs.add(song)
            playlist_obj.save()
            return redirect('song:show_songs')

        return render(request,'songs/detail.html' )


class CreateSong(UserPassesTestMixin, CreateView):
    form_class = SongForm
    template_name ="songs/song_form.html"
    success_url = '/songs/'

    def test_func(self):
        return self.request.user.is_superuser



class UpdateSong(UserPassesTestMixin, UpdateView):
    form_class = SongForm
    model = Song
    template_name ="songs/song_edit.html"
    
    def test_func(self):
        return self.request.user.is_superuser

class DeleteSong(UserPassesTestMixin, DeleteView):
    model = Song
    success_url = reverse_lazy('song:show_songs')
    
    def test_func(self):
        return self.request.user.is_superuser