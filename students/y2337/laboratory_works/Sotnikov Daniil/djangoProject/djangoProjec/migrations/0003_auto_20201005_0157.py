# Generated by Django 3.1.2 on 2020-10-04 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoProjec', '0002_auto_20201005_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='stops',
            field=models.IntegerField(default=0),
        ),
    ]
