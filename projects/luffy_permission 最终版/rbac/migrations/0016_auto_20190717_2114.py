# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-17 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0015_auto_20190717_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='weight',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='权重'),
        ),
    ]
