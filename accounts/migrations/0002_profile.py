# Generated by Django 4.1.6 on 2023-05-11 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_guide', models.BooleanField(default=False)),
                ('verification_status', models.CharField(choices=[('NOT VERIFIED', 'Непроверен'), ('SENT TO VERIFICATION', 'Отправлен на проверку'), ('SENT TO REVIEW', 'Отправлен на доработку'), ('CONFIRMED', 'Подтвержден'), ('REFUSE', 'Отказ')], default='NOT VERIFIED', max_length=256)),
                ('current_location', models.CharField(blank=True, max_length=512, null=True)),
                ('birthdate', models.DateField()),
                ('languages', models.CharField(blank=True, max_length=512, null=True, verbose_name='Языки')),
                ('about', models.TextField(blank=True, max_length=2048, null=True, verbose_name='О себе')),
                ('experience_resume', models.FileField(blank=True, null=True, upload_to='experience_resumes', verbose_name='Резюме с опытом')),
                ('certificates', models.FileField(blank=True, null=True, upload_to='certificates', verbose_name='Сертификаты')),
                ('bank_details', models.CharField(max_length=512)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]