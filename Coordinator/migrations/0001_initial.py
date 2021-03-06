# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-04 21:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0007_auto_20170914_1203'),
        ('Students', '0004_auto_20170924_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creationDate', models.DateField(auto_now_add=True)),
                ('ActiveDate', models.DateField()),
                ('DeactiveDate', models.DateField()),
                ('is_active', models.BooleanField(default=False)),
                ('scientist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Assigned_scientist', to='registration.UserProfileInfo')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Assigned_student', to='Students.Student')),
            ],
        ),
    ]
