# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matrimonyapp', '0003_auto_20181009_1533'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Register',
        ),
    ]
