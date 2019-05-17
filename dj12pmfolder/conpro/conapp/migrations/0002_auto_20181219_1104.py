# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-19 05:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='condata',
            name='email',
            field=models.EmailField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='condata',
            name='number',
            field=models.BigIntegerField(max_length=30),
        ),
    ]