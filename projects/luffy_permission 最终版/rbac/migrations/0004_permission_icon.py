# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-12 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0003_auto_20190712_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='icon',
            field=models.CharField(default=1, max_length=100, verbose_name='图标'),
            preserve_default=False,
        ),
    ]
