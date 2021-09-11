# Generated by Django 3.0.1 on 2020-09-02 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0011_auto_20200902_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, verbose_name='Название товара')),
                ('product_size', models.CharField(default='Стандарт', max_length=200, verbose_name='Размер товара')),
                ('product_color', models.CharField(default='Не указан', max_length=200, verbose_name='Цвет товара')),
                ('product_photo', models.ImageField(blank=True, upload_to='products_photo/', verbose_name='Фотография товара')),
                ('remained_amount', models.PositiveIntegerField(verbose_name='Количество оставшегося товара')),
                ('price', models.PositiveIntegerField(verbose_name='Цена товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='BoughtProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bought_date', models.DateField(auto_now_add=True, verbose_name='Дата покупки')),
                ('given', models.BooleanField(default=False, verbose_name='Выдан ли товар покупателю')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.Puples', verbose_name='Покупатель товара')),
                ('main_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.MarketProduct', verbose_name='Ссылка на основной товар')),
            ],
            options={
                'verbose_name': 'Купленный товар',
                'verbose_name_plural': 'Купленные товары',
            },
        ),
    ]