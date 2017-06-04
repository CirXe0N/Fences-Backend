# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-04 21:26
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameRoom',
            fields=[
                ('created_at', models.DateTimeField(auto_created=True)),
                ('room_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('player_one', models.UUIDField(editable=False)),
                ('player_one_reply_channel', models.CharField(max_length=50, null=True)),
                ('player_two', models.UUIDField(null=True)),
                ('player_two_reply_channel', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
