from rest_framework import serializers
from api.agendamentos.models import Agendamento



class AgendamentoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = ('id', 'nome_paciente', 'data', 'hora_inicio', 'hora_final', 'procedimento')
