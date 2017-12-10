from django.test import TestCase

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

