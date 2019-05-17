# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-28 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('feedback', models.CharField(max_length=500)),
            ],
        ),
    ]
