# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-11 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimonyapp', '0008_remove_register_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='height',
            field=models.FloatField(null=True),
        ),
    ]
