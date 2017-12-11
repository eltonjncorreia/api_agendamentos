from django.test import TestCase
from django.urls import reverse, resolve

from api.agendamentos.views import AgendamentosViewSet


class ResolveNomeGetAndPostTest(TestCase):
    def setUp(self):
        self.resolveLista = self.resolver_nomes('agenda:listagem')
        self.resolveDetail = self.resolver_nomes('agenda:detalhe', pk=1)


    def test_resolve_url_lista(self):
        self.assertEqual(self.resolveLista.func.cls, AgendamentosViewSet)


    def test_resolve_url_action_lista(self):
        self.assertIn('get', self.resolveLista.func.actions)
        self.assertEqual('list', self.resolveLista.func.actions['get'])

    def test_resolve_url_recupera_detail(self):
        self.assertEqual(self.resolveDetail.func.cls, AgendamentosViewSet)

    def test_resolve_url_recupera_action_detail(self):
        self.assertIn('get', self.resolveDetail.func.actions)
        self.assertEqual('retrieve', self.resolveDetail.func.actions['get'])

    def resolver_nomes(self, name, **kwargs):
        url = reverse(name,  kwargs=kwargs)
        return resolve(url)



