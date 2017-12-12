from rest_framework import viewsets

from api.agendamentos.models import Agendamento
from api.agendamentos.serializers import AgendamentoSerializers

# Create your views here.

class AgendamentosViewSet(viewsets.ModelViewSet):
    """
    Esta view fornece automaticamente `list`,` create`, `retrieve`,
    ações de "atualização" e "destruir".

    """
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializers
