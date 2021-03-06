# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-14 17:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import scientist.models


class Migration(migrations.Migration):

    dependencies = [
        ('scientist', '0005_auto_20170914_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userletters',
            name='letterfile',
            field=models.FileField(blank=True, upload_to=scientist.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='userletters',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
