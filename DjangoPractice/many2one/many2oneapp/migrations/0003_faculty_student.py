# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-25 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('many2oneapp', '0002_auto_20190125_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='student',
            field=models.ManyToManyField(to='many2oneapp.Student'),
        ),
    ]
