# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-04 10:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_auto_20170203_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album_title',
        ),
    ]
