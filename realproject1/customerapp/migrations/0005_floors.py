# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-19 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0004_auto_20200219_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Floors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
    ]