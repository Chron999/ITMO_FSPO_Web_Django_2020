# Generated by Django 3.0.8 on 2020-07-27 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='film_studio',
        ),
        migrations.RemoveField(
            model_name='book',
            name='number_group',
        ),
        migrations.RemoveField(
            model_name='book',
            name='number_of_student',
        ),
        migrations.RemoveField(
            model_name='book',
            name='poster',
        ),
    ]
