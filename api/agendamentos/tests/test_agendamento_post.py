from django.test import TestCase
from django.shortcuts import resolve_url as r
from api.agendamentos.models import Agendamento


class AgendamentosPostTest(TestCase):
    def setUp(self):
        self.obj = Agendamento.objects.create(
            nome_paciente='elton jefferson',
            procedimento='testando a pressão',
            data='1988-12-12',
            hora_inicio='12:00:20',
            hora_final='12:40:20',

        )

    def test_post_create(self):
        self.assertTrue(Agendamento.objects.exists())

    # def test_post_create_201(self):
    #     """ verify POST should """
    #     dados = dict(nome_paciente="Elton Jefferson",
    #                  data='1988-10-10',
    #                  hora_inicio='12:00',
    #                  hora_final='13:00',
    #                  procedimento='Exame de pressão' )
    #
    #     self.response = self.client.post(r('agenda:create'), dados)
    #     self.assertEqual(201, self.response.status_code )