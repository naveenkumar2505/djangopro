# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-02-02 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegstrationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('second_name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=150)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
