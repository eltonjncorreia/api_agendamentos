from rest_framework import viewsets

from api.agendamentos.models import Agendamento
from api.agendamentos.serializers import AgendamentoSerializers

# Create your views here.

class AgendamentosViewSet(viewsets.ModelViewSet):
    """

    Esta API fornece automaticamente `list`,` create`, `retrieve`,
    ações de "atualização" e "destruir".

    retrieve:
    Recupera os detalhes de um agendamento
    URL http://localhost:8000/agendamentos/detalhes/1/

    list:
    Retorna uma lista de todos os agendamentos.
    URL http://localhost:8000/agendamentos/

    create:
    Cria um novo agendamento.
    URL http://localhost:8000/agendamentos/agendar/

    update:
    Atualiza um agendamento
    URL http://localhost:8000/agendamentos/remarcar/1/

    destroy:
    Excluir um agendamento
    URL http://localhost:8000/agendamentos/cancelar/1/


    """
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializers
