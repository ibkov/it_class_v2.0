# Generated by Django 3.0.1 on 2020-09-01 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_boughtproduct_given'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boughtproduct',
            options={'verbose_name': 'Купленный товар', 'verbose_name_plural': 'Купленные товары'},
        ),
    ]