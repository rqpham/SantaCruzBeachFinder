# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 04:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beaches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beach',
            name='has_free_parking',
            field=models.BooleanField(default=False),
        ),
    ]