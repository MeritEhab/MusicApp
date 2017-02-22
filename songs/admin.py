from django.contrib import admin

from songs import models
# Register your models here.

class SongsAdmin(admin.ModelAdmin):
    list_display = [
        'artist',
        'song_title'
        ]
    list_filter = [
        'artist',
        'genre'
        ]
    
admin.site.register(models.Song , SongsAdmin)
