# Generated by Django 4.2.1 on 2023-05-16 11:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('description', models.TextField(max_length=3000, verbose_name='Описание')),
                ('start_date', models.DateTimeField(verbose_name='Дата старта')),
                ('end_date', models.DateTimeField(verbose_name='Дата завершения')),
                ('language', models.CharField(max_length=300, verbose_name='Язык проведения')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000)], verbose_name='Стоимость')),
                ('max_number_of_tourists', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(250)], verbose_name='Максимальное количество туристов')),
                ('min_number_of_tourists', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(250)], verbose_name='Минимальное количество туристов')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
    ]
