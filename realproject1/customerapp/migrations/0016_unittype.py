# Generated by Django 3.0.3 on 2020-03-04 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0015_amenities'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
    ]
