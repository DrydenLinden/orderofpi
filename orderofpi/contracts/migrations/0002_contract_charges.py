# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='charges',
            field=models.CharField(default='Null', max_length=500),
            preserve_default=False,
        ),
    ]
