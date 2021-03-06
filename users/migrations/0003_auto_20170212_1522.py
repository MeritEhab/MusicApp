# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 15:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_playlist_songs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='fk_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(blank=True, null=True, to='songs.Song', verbose_name='Songs'),
        ),
    ]
