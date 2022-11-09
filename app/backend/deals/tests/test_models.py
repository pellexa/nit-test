from django.test import TestCase
from ..models import Counterparty, DeliveryPoint, Deal
import datetime
import pytz

class CounterpartyTest(TestCase):
    """ Test module for Counterparty model """

    def setUp(self):
        deliveryPoint1 = DeliveryPoint.objects.create(name='VIP Bereg')
        deliveryPoint2 = DeliveryPoint.objects.create(name='VTP Austria')
        counterparty1 = Counterparty.objects.create(name='Контрагент1', rating='BBB')
        counterparty2 = Counterparty.objects.create(name='Контрагент2', rating='B-') 

        Deal.objects.create(
            type = 'esp',
            dateDeal = datetime.datetime(2021, 1, 5, 0, 0, 0, 0, tzinfo=pytz.UTC),
            deliveryPoint = deliveryPoint1,
            volume = 10,
            price =  24.095, 
            deliveryStart = datetime.datetime(2022, 1, 1, 0, 0, 0, 0, tzinfo=pytz.UTC),
            deliveryEnd = datetime.datetime(2023, 1, 1, 0, 0, 0, 0, tzinfo=pytz.UTC),
            tool = '2022',
            counterparty = counterparty1,
        )
        Deal.objects.create(
            type = 'efet',
            dateDeal = datetime.datetime(2021, 1, 19, 0, 0, 0, 0, tzinfo=pytz.UTC),
            deliveryPoint = deliveryPoint2,
            volume = 30,
            price =  17.820, 
            deliveryStart = datetime.datetime(2021, 4, 1, 0, 0, 0, 0, tzinfo=pytz.UTC),
            deliveryEnd = datetime.datetime(2021, 7, 1, 0, 0, 0, 0, tzinfo=pytz.UTC),
            tool = '2021-Q2',
            counterparty = counterparty2,
        ) 

    def test_deal(self):
        deal1 = Deal.objects.get(type = 'esp')
        deal2 = Deal.objects.get(type = 'efet')
        self.assertNotEqual(deal1, deal2)
