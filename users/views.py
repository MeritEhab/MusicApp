from django.views.generic import (
    ListView, DetailView, 
    CreateView, UpdateView,
    DeleteView
    )
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User


from songs.models import Song
from .forms import PlaylistForm
from .models import PlayList

class ListPlaylists(ListView):
    model = PlayList
    template_name ="playlist/playlists.html"
    def get_queryset(self):
        queryset = PlayList.objects.filter(fk_user=self.request.user)
        return queryset

class DetailPlaylist(DetailView):
    model = PlayList
    template_name ="playlist/playlist_details.html"


class CreatePlaylist(CreateView):
    form_class = PlaylistForm

    template_name ="playlist/playlist_form.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.fk_user = self.request.user
        obj.save()        

        return redirect("user:playlist_list")
        
class UpdatePlaylist(UpdateView):
    form_class = PlaylistForm
    model = PlayList
    template_name ="playlist/playlist_edit.html"
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.fk_user = self.request.user
        obj.save()
        return redirect("user:playlist_list")

class DeletePlaylist(DeleteView):
    model = PlayList
    success_url = reverse_lazy('user:playlist_list')
