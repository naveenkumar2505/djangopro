# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-02 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('httpapp', '0004_auto_20190217_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
