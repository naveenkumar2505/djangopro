# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-09 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimonyapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='weight',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='register',
            name='mobile',
            field=models.CharField(max_length=20),
        ),
    ]