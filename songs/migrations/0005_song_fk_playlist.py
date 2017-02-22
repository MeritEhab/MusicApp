# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-04 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('songs', '0004_remove_song_album_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='fk_playlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.PlayList', verbose_name='Play List'),
        ),
    ]