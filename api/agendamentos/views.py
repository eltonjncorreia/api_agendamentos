from rest_framework import viewsets
from api.agendamentos.models import Agendamento
from api.agendamentos.serializers import AgendamentoSerializers

# Create your views here.

class AgendamentosViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializers
