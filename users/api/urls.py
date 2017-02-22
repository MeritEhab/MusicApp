from django.conf.urls import url

from . import views
app_name = 'user'

urlpatterns = [
    url(r'^playlists/$', views.PlaylistCreateListAPIView.as_view(), name='user-playlists-list'),
    url(r'^playlists/(?P<pk>\d+)/$',views.PlaylistDetailAPIView.as_view(),name='playlist_details')

]