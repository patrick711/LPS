# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-24 21:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0002_auto_20170924_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='scientist',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Assigned_scientist', to=settings.AUTH_USER_MODEL),
        ),
    ]
