# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-20 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0013_auto_20200220_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitcreation',
            name='flatno',
            field=models.IntegerField(),
        ),
    ]