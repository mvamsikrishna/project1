# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temperature', '0003_humidity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moisture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hum_value', models.CharField(max_length=250)),
            ],
        ),
    ]