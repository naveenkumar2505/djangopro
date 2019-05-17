# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-03 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('userName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('salary', models.BigIntegerField()),
                ('dob', models.DateField()),
                ('role', models.CharField(max_length=50)),
            ],
        ),
    ]