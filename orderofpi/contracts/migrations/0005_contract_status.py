# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-21 21:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0004_auto_20170712_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('completed', 'Completed'), ('rejected', 'Rejected')], default='pending', max_length=15),
        ),
    ]