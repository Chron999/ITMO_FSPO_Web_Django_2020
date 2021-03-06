# Generated by Django 3.1.3 on 2020-11-03 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название Компании')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameProd', models.CharField(max_length=30, verbose_name='Название продукта')),
                ('varProd', models.CharField(choices=[('Шампунь', 'Шампунь'), ('Туалетная вода', 'Туалетная вода'), ('Парфюм', 'Парфюм')], max_length=30, verbose_name='Тип Товара')),
                ('priceProd', models.PositiveIntegerField(verbose_name='Цена Продукта')),
                ('expProd', models.DateField()),
                ('idComp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company', verbose_name='Компания-Поставщик')),
            ],
        ),
        migrations.CreateModel(
            name='Mackler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surMac', models.CharField(max_length=30, verbose_name='Фамилия Маклера')),
                ('adrMac', models.CharField(max_length=30, verbose_name='Адресс Маклера')),
                ('idMac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company', verbose_name='Маклер')),
            ],
        ),
    ]
