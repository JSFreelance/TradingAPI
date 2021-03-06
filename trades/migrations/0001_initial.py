# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-11 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SellCurrency', models.CharField(default='EUR', max_length=3)),
                ('SellAmount', models.FloatField()),
                ('BuyCurrency', models.CharField(default='EUR', max_length=3)),
                ('BuyAmount', models.FloatField(default=0.0)),
                ('Rate', models.FloatField(default=1.0)),
                ('BookingDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
