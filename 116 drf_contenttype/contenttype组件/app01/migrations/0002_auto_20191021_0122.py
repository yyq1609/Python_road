# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-21 01:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricepolicy',
            name='object_id',
            field=models.IntegerField(verbose_name='表里的ID'),
        ),
        migrations.AlterField(
            model_name='pricepolicy',
            name='table_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='关联表名称'),
        ),
    ]
