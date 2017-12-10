from django.contrib import admin
from api.agendamentos.models import Agendamento
# Register your models here.

class AgendamentoModelAdmin(admin.ModelAdmin):
    list_display = ('nome_paciente', 'procedimento', 'data', 'hora_inicio', 'hora_final')
    list_filter = ('nome_paciente', 'procedimento', 'data')
    search_fields = ('nome_paciente', 'procedimento')

admin.site.register(Agendamento, AgendamentoModelAdmin)