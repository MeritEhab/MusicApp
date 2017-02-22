from django.conf.urls import url

from . import views

app_name = 'song'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$',views.SongDetialAPIView.as_view(),name='detial'),
    url(r'^$',views.SongCreateAPIView.as_view(),name='add_song'),

]

