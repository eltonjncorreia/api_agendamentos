# Generated by Django 2.0 on 2017-12-09 21:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0012_auto_20171209_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='data',
            field=models.DateField(blank=True, default=datetime.datetime.utcnow, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.datetime(2017, 12, 9, 21, 8, 4, 966095), verbose_name='Fim'),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.datetime(2017, 12, 9, 21, 8, 4, 966058), verbose_name='Inicio'),
        ),
    ]
