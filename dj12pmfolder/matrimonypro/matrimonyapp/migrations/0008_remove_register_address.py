# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matrimonyapp', '0007_auto_20181108_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='address',
        ),
    ]
