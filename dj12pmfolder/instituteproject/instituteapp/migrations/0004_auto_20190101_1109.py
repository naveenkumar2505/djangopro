# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-01 05:39
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('instituteapp', '0003_auto_20190101_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='cources',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('restapi', 'RESTAPI'), ('python', 'PYTHON'), ('django', 'DJANGO'), ('ui', 'UI')], max_length=100),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='timing',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('evening', 'EVENING'), ('morning', 'MORNING'), ('afternoon', 'AFTERNOON')], max_length=100),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='trainer',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('nani', 'NANI'), ('raj', 'RAJ'), ('narayana', 'NARAYANA'), ('prakash', 'PRAKASH')], max_length=100),
        ),
    ]
