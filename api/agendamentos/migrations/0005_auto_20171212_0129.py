# Generated by Django 2.0 on 2017-12-12 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0004_auto_20171212_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='hora_final',
            field=models.TimeField(default=1, verbose_name='Fim'),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='hora_inicio',
            field=models.TimeField(default=1, verbose_name='Inicio'),
        ),
    ]
