# Generated by Django 2.0 on 2017-12-09 20:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0004_auto_20171209_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='hora_final',
            field=models.TextField(blank=True, default=django.utils.timezone.now, verbose_name='Fim'),
        ),
    ]
