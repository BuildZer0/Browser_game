# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-01 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_gamesession_players'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='state',
            field=models.CharField(blank=True, default='in_lobby', max_length=100),
        ),
    ]
