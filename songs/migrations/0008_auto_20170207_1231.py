# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0007_auto_20170207_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(default='', upload_to=b'', verbose_name='Audio File'),
        ),
    ]
