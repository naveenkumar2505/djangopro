# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-02-17 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('httpapp', '0003_auto_20190130_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
