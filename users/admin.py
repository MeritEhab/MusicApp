from django.contrib import admin

from users import models

class PlaylistAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'fk_user'
        ]
    
# Register your models here.

admin.site.register(models.PlayList , PlaylistAdmin)
