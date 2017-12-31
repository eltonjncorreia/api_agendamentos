from django.test import TestCase
from django.shortcuts import resolve_url as r


class AgendamentosTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('agenda:listagem'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)


