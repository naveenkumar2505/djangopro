# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-24 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dropdownapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drop',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=2, max_length=128),
            preserve_default=False,
        ),
    ]
