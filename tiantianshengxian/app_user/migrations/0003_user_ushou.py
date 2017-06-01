# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0002_auto_20170601_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ushou',
            field=models.CharField(max_length=20),
            # field=models.CharField(default='', max_length=20),
            # preserve_default=False,
        ),
    ]
