import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Counterparty, DeliveryPoint, Deal
from ..serializers import DealSerializer
import datetime
import pytz

# initialize the APIClient app
client = Client()

class GetAllDealsTest(TestCase):
    """ Test module for GET all deals API """

    def setUp(self):
        deliveryPoint1 = DeliveryPoint.objects.create(name='VIP Bereg')
        deliveryPoint2 = DeliveryPoint.objects.create(name='VTP Austria')
        counterparty1 = Counterparty.objects.create(name='Контрагент1', rating='BBB')
        counterparty2 = Counterparty.objects.create(name='Контрагент2', rating='B-') 

        self.deal1 = Deal.objects.create(
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
        self.deal2 = Deal.objects.create(
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

    def test_get_all_deals(self):
        # get API response
        response = client.get(reverse('get_post_deals'))
        # get data from db
        deals = Deal.objects.all()
        serializer = DealSerializer(deals, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_deal(self):
        response = client.get(
            reverse('get_delete_update_deal', kwargs={'id': self.deal1.id}))
        deal = Deal.objects.get(id=self.deal1.id)
        serializer = DealSerializer(deal)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_deal(self):
        response = client.get(
            reverse('get_delete_update_deal', kwargs={'id': 9999999999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewDealTest(TestCase):
    """ Test module for inserting a new deal """

    def setUp(self):
        self.deliveryPoint = DeliveryPoint.objects.create(name='VIP Bereg')
        self.counterparty = Counterparty.objects.create(name='Контрагент1', rating='BBB')

        self.valid_payload = {
            "type":"esp",
            "dateDeal":"2021-01-05T00:00:00Z",
            "deliveryPoint": self.deliveryPoint.id,
            "volume":10,
            "price":"24.095",
            "deliveryStart":"2022-01-01T00:00:00Z",
            "deliveryEnd":"2023-01-01T00:00:00Z",
            "tool":"2022",
            "counterparty": self.counterparty.id
        }
        
        self.duplicate_payload = {
            "type":"esp",
            "dateDeal":"2021-01-05T00:00:00Z",
            "deliveryPoint": self.deliveryPoint.id,
            "volume":10,
            "price":"24.095",
            "deliveryStart":"2022-01-01T00:00:00Z",
            "deliveryEnd":"2023-01-01T00:00:00Z",
            "tool":"2022",
            "counterparty": self.counterparty.id
        }

    def test_create_valid_deal(self):
        response = client.post(
            reverse('get_post_deals'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_deal(self):
        response = client.post(
            reverse('get_post_counterparties'),
            data=json.dumps(self.duplicate_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleDealTest(TestCase):
    """ Test module for updating an existing deal record """

    def setUp(self):
        self.counterparty1 = Counterparty.objects.create(name='Контрагент1', rating='BB-')
        self.counterparty2 = Counterparty.objects.create(name='Контрагент2', rating='CCC')
        self.deliveryPoint1 = DeliveryPoint.objects.create(name='VIP Bereg')
        self.deliveryPoint2 = DeliveryPoint.objects.create(name='VTP Austria')

        self.deal = Deal.objects.create(
            type = 'esp',
            dateDeal = datetime.datetime(2021, 1, 5, 0, 0, 0, 0, tzinfo=pytz.UTC),
            deliveryPoint = self.deliveryPoint1,
            volume = 10,
            price =  24.095, 
            deliveryStart = datetime.datetime(2022, 1, 1, 0, 0, 0, 0, tzinfo=pytz.UTC),
            deliveryEnd = datetime.datetime(2023, 1, 1, 0, 0, 0, 0, tzinfo=pytz.UTC),
            tool = '2022',
            counterparty = self.counterparty1,
        )

        self.valid_payload = {
            "type":"esp",
            "dateDeal":"2021-01-05T00:00:00Z",
            "deliveryPoint": self.deliveryPoint2.id,
            "volume":100,
            "price":"240.095",
            "deliveryStart":"2022-01-01T00:00:00Z",
            "deliveryEnd":"2023-01-01T00:00:00Z",
            "tool":"2022",
            "counterparty": self.counterparty2.id
        }
        self.invalid_payload = {
            "type":"",
            "dateDeal":"2021-01-05T00:00:00Z",
            "deliveryPoint": self.deliveryPoint2.id,
            "volume":100,
            "price":"240.095",
            "deliveryStart":"2022-01-01T00:00:00Z",
            "deliveryEnd":"2023-01-01T00:00:00Z",
            "tool":"2022",
            "counterparty": self.counterparty2.id
        }

    def test_valid_update_deal(self):
        response = client.put(
            reverse('get_delete_update_deal', kwargs={'id': self.deal.id}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_deal(self):
        response = client.put(
            reverse('get_delete_update_deal', kwargs={'id': self.deal.id}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleDealTest(TestCase):
    """ Test module for deleting an existing deal record """

    def setUp(self):
        self.counterparty = Counterparty.objects.create(name='Контрагент1', rating='CCC')
        self.deliveryPoint = DeliveryPoint.objects.create(name='VIP Bereg')

        self.deal = Deal.objects.create(
            type = 'esp',
            dateDeal = datetime.datetime(2021, 1, 5, 0, 0, 0, 0, tzinfo=pytz.UTC),
            deliveryPoint = self.deliveryPoint,
            volume = 10,
            price =  24.095, 
            deliveryStart = datetime.datetime(2022, 1, 1, 0, 0, 0, 0, tzinfo=pytz.UTC),
            deliveryEnd = datetime.datetime(2023, 1, 1, 0, 0, 0, 0, tzinfo=pytz.UTC),
            tool = '2022',
            counterparty = self.counterparty,
        )

    def test_valid_delete_deal(self):
        response = client.delete(
            reverse('get_delete_update_deal', kwargs={'id': self.deal.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_delete_deal(self):
        response = client.delete(
            reverse('get_delete_update_deal', kwargs={'id': 9999999999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
