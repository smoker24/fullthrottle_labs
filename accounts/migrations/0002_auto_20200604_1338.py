# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-04 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='time_zone',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
