# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-12 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currency',
            name='id',
        ),
        migrations.AlterField(
            model_name='currency',
            name='text',
            field=models.CharField(max_length=3, primary_key=True, serialize=False),
        ),
    ]
