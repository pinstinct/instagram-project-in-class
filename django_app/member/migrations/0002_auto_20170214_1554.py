# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 06:54
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='myuser',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
