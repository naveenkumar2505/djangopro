# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-01 05:32
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('instituteapp', '0002_auto_20181231_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='cources',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('python', 'PYTHON'), ('django', 'DJANGO'), ('restapi', 'RESTAPI'), ('ui', 'UI')], max_length=100),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='timing',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('afternoon', 'AFTERNOON'), ('morning', 'MORNING'), ('evening', 'EVENING')], max_length=100),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='trainer',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('prakash', 'PRAKASH'), ('nani', 'NANI'), ('raj', 'RAJ'), ('narayana', 'NARAYANA')], max_length=100),
        ),
    ]
