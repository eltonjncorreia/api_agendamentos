from django.test import TestCase
from django.shortcuts import resolve_url as r
from api.agendamentos.models import Agendamento


class AgendamentosDetailTest(TestCase):
    def setUp(self):
        self.obj = Agendamento.objects.create(
            nome_paciente='elton jefferson',
            procedimento='testando a pressão',
            data='1988-12-12',
            hora_inicio='12:00:20',
            hora_final='12:40:20',

        )
        self.response = self.client.get(r('agenda:detalhe', self.obj.pk))

    def test_get_detail_id(self):
        self.assertEqual(200, self.response.status_code)


class AgendamentoDetailNotFound(TestCase):
    def test_not_found(self):
        self.response = self.client.get(r('agenda:detalhe', 0))
        self.assertEqual(404, self.response.status_code)
