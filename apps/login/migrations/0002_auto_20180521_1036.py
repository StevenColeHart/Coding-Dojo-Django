# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-21 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='alias',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='birth_day',
            field=models.DateField(blank=True, null=True),
        ),
    ]
