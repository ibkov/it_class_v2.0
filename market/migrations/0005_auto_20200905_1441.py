# Generated by Django 3.0.1 on 2020-09-05 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_boughtproduct_given_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boughtproduct',
            name='given_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата выдачи товара'),
        ),
    ]
