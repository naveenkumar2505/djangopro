# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-27 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taskapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_name',
            field=models.CharField(max_length=256, verbose_name='Customer name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=50, verbose_name='product Name'),
        ),
    ]
