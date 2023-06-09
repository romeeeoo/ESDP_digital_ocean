# Generated by Django 4.2.2 on 2023-06-09 12:32

from django.db import migrations, models
import tours.models.tour


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='end_date',
            field=models.DateTimeField(validators=[tours.models.tour.date_validation], verbose_name='Дата завершения'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='moderation_status',
            field=models.CharField(choices=[('NOT VERIFIED', 'Непроверен'), ('SENT TO VERIFICATION', 'Отправлен на проверку'), ('SENT TO REWORK', 'Отправлен на доработку'), ('CONFIRMED', 'Подтвержден'), ('REFUSED', 'Отказ'), ('FINISHED', 'Завершён'), ('STARTED', 'Начался')], default='NOT VERIFIED', max_length=256),
        ),
        migrations.AlterField(
            model_name='tour',
            name='start_date',
            field=models.DateTimeField(validators=[tours.models.tour.date_validation], verbose_name='Дата старта'),
        ),
    ]