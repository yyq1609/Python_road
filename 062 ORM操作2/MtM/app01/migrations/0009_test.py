# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-25 11:45
from __future__ import unicode_literals

import app01.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_auto_20190625_0851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', app01.models.MyCharField(max_length=20)),
            ],
        ),
    ]
