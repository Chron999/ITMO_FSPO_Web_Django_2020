# Generated by Django 3.1.2 on 2020-11-01 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoshow', '0006_auto_20201101_0555'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshops',
            name='workshop_closetime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workshops',
            name='workshop_opentime',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
