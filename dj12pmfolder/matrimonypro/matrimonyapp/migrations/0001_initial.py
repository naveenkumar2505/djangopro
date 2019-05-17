# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-06 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=20)),
                ('mname', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('mobile', models.IntegerField()),
                ('phote', models.ImageField(upload_to='images')),
            ],
        ),
    ]
