# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matrimonyapp', '0005_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='salary',
            field=models.IntegerField(null=True),
        ),
    ]
