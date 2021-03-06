
from django.db import models

# Create your models here.
from _datetime import datetime


class Agendamento(models.Model):
    data = models.DateField('Data', default=datetime.now().date)
    hora_inicio = models.TimeField('Inicio', default=datetime.now().hour)
    hora_final = models.TimeField('Fim', default=datetime.now().hour)
    nome_paciente = models.CharField('Paciente', blank=True, max_length=150)
    procedimento = models.CharField('Procedimento',blank=True, max_length=250)

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"


    def __str__(self):
        return self.nome_paciente

