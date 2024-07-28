# Generated by Django 5.0.4 on 2024-05-18 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicApp', '0005_doctor_groups_doctor_is_active_doctor_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='working_days',
            field=models.CharField(default='Пон, Вто, Сре, Чет, Пят, Суб, Вос', max_length=28),
        ),
    ]