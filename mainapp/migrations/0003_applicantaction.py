# Generated by Django 3.0.6 on 2020-05-24 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20200523_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='', verbose_name='Дата собеседования')),
                ('time', models.TimeField(default='', verbose_name='Время собеседования')),
                ('url', models.URLField(default='', verbose_name='Ссылка собесодования')),
                ('login', models.CharField(default='', max_length=30, verbose_name='Идентификатор собеседования')),
                ('password', models.CharField(default='', max_length=50, verbose_name='Пароль собеседования')),
                ('check', models.BooleanField(default=False, verbose_name='Подтверждение ученика')),
                ('action_app', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.Puples')),
            ],
            options={
                'verbose_name': 'Для кандидатов',
                'verbose_name_plural': 'Для кандидатов',
            },
        ),
    ]
