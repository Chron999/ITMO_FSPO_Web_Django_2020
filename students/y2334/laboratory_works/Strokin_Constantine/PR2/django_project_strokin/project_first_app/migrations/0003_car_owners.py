# Generated by Django 3.1.1 on 2020-10-06 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0002_auto_20201007_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='owners',
            field=models.ManyToManyField(through='project_first_app.Possession', to='project_first_app.Owner'),
        ),
    ]
