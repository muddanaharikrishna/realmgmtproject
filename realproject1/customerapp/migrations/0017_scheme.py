# Generated by Django 3.0.3 on 2020-03-04 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0016_unittype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
    ]