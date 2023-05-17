from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Tour(models.Model):
    author = models.ForeignKey(
        null=False,
        to=get_user_model(),
        related_name='tour',
        blank=False,
        verbose_name='Автор',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name='Название',
    )
    description = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
        verbose_name='Описание',
    )
    start_date = models.DateField(
        auto_now_add=False,
        auto_now=False,
        verbose_name='Дата старта',
    )
    end_date = models.DateField(
        auto_now_add=False,
        auto_now=False,
        verbose_name='Дата завершения',
    )
    language = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name='Язык проведения',
    )
    price = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(1000000)],
        verbose_name='Стоимость',
    )
    max_number_of_tourists = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(250)],
        verbose_name='Максимальное количество туристов',
    )
    min_number_of_tourists = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(250)],
        verbose_name='Минимальное количество туристов',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата и время обновления',
    )

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'

    def __str__(self):
        return f'Tour {self.title} by {self.author}'