# Generated by Django 5.0.4 on 2024-05-18 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicApp', '0002_alter_patient_iin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='iin',
            field=models.CharField(primary_key=True, serialize=False, unique=True, verbose_name='IIN'),
        ),
    ]