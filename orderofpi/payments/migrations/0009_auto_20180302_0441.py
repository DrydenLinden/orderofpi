# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-02 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0008_merge_20170725_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='recipient',
            field=models.CharField(default='ess', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(blank=True, choices=[('succeeded', 'Succeeded'), ('pending', 'Pending'), ('failed', 'Failed'), ('cancelled', 'Cancelled'), ('refunded', 'Refunded')], max_length=50),
        ),
    ]
