# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_contract_charges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='charges',
            field=models.TextField(),
        ),
    ]
