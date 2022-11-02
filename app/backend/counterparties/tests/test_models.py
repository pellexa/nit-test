from django.test import TestCase
from ..models import Counterparty


class CounterpartyTest(TestCase):
    """ Test module for Counterparty model """

    def setUp(self):
        Counterparty.objects.create(
            name='Контрагент1', rating='BBB')
        Counterparty.objects.create(
            name='Контрагент2', rating='B-') 

    def test_counterparty(self):
        counterparty1 = Counterparty.objects.get(name='Контрагент1')
        counterparty2 = Counterparty.objects.get(name='Контрагент2')
        self.assertNotEqual(counterparty1, counterparty2)
