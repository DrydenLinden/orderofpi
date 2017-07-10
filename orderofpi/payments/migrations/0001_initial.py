# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 21:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('online_cc', 'Online Credit Card'), ('offline_cc', 'In Office Credit Card'), ('cash', 'Cash')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('stripe_status', models.CharField(max_length=50, null=True)),
                ('stripe_id', models.CharField(max_length=20, null=True)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contracts.Contract')),
            ],
        ),
    ]
