# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-30 14:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('httpapp', '0002_auto_20190108_2045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='last_name',
            new_name='lastname',
        ),
    ]
