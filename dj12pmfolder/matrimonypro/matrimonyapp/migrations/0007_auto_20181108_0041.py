# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matrimonyapp', '0006_auto_20181108_0032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='password1',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='register',
            name='password2',
        ),
    ]
