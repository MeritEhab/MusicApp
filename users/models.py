from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from songs.models import Song


# Create your models here.

class PlayList(models.Model):

    name = models.CharField(max_length=100, verbose_name=("Play List Name"))
    songs = models.ManyToManyField(Song, verbose_name=("Songs"), null=True, blank=True)
    fk_user = models.ForeignKey(User, verbose_name=("User"))

   
    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('user:playlist_details',kwargs={'pk':self.pk})

