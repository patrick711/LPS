# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-01 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20170831_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='is_being_matched',
            field=models.BooleanField(default=False),
        ),
    ]