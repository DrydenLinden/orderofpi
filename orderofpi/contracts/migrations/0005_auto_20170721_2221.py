# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-21 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0004_auto_20170712_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='extend_id',
            field=models.CharField(blank=True, max_length=60, null=True, unique=True),
        ),
    ]
