# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-18 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
