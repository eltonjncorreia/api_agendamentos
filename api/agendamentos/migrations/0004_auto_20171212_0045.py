# Generated by Django 2.0 on 2017-12-12 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0003_auto_20171211_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='hora_final',
            field=models.TimeField(default=0, verbose_name='Fim'),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='hora_inicio',
            field=models.TimeField(default=0, verbose_name='Inicio'),
        ),
    ]