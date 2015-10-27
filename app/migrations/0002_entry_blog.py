# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='blog',
            field=models.ForeignKey(to='app.Blog', default=1),
            preserve_default=False,
        ),
    ]
