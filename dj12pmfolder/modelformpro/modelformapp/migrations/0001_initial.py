# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-25 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelFormData',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('sal', models.IntegerField()),
                ('loc', models.CharField(max_length=100)),
            ],
        ),
    ]
