from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Song(models.Model):
    genre_options = (
        ('rock', ('Rock')),
        ('pop', ('Pop')),
        ('hiphop', ('HipHop')),
        ('jazz', ('Jazz')),
        ('classic', ('Classic')),
    )
    song_title = models.CharField(max_length=100, verbose_name=("Song Title"))
    artist = models.CharField(max_length=100, verbose_name=("Artist"))
    genre = models.CharField(max_length=50, verbose_name=("Genre"), choices=genre_options)
    audio_file = models.FileField(default='',verbose_name=("Audio File"))
    logo = models.FileField(default='',verbose_name=("Logo"), null=True, blank=True)

    def __unicode__(self):
        return self.artist+'-'+self.song_title

    def get_absolute_url(self):
        return reverse('song:song_detial',kwargs={'pk':self.pk})