# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-11 23:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='creat_time',
            new_name='create_time',
        ),
    ]