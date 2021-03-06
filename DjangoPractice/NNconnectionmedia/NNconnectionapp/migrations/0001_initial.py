# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-02 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(help_text='Enter FirstName', max_length=100, null=True)),
                ('surname', models.CharField(help_text='Enter LastName', max_length=100, null=True)),
                ('email', models.EmailField(max_length=256)),
                ('number', models.BigIntegerField()),
                ('password', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=5)),
            ],
        ),
    ]
