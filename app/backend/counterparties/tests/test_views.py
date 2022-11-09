import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Counterparty
from ..serializers import CounterpartySerializer


# initialize the APIClient app
client = Client()


class GetAllCounterpartiesTest(TestCase):
    """ Test module for GET all counterparties API """

    def setUp(self):
        self.counterparty1 = Counterparty.objects.create(name='Контрагент1', rating='BBB')
        self.counterparty2 = Counterparty.objects.create(name='Контрагент2', rating='B-')
        self.counterparty3 = Counterparty.objects.create(name='Контрагент3', rating='CCC')
        self.counterparty4 = Counterparty.objects.create(name='Контрагент4', rating='BB-')

    def test_get_all_counterparties(self):
        # get API response
        response = client.get(reverse('get_post_counterparties'))
        # get data from db
        counterparties = Counterparty.objects.all()
        serializer = CounterpartySerializer(counterparties, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_counterparty(self):
        response = client.get(
            reverse('get_delete_update_counterparty', kwargs={'id': self.counterparty1.id}))
        counterparty = Counterparty.objects.get(id=self.counterparty1.id)
        serializer = CounterpartySerializer(counterparty)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_counterparty(self):
        response = client.get(
            reverse('get_delete_update_counterparty', kwargs={'id': 9999999999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewСounterpartyTest(TestCase):
    """ Test module for inserting a new counterparty """

    def setUp(self):
        self.valid_payload = {'name': 'Контрагент1', 'rating': 'BB-'}
        self.invalid_payload = {'name': '', 'rating': 'CCC'}

    def test_create_valid_counterparty(self):
        response = client.post(
            reverse('get_post_counterparties'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_counterparty(self):
        response = client.post(
            reverse('get_post_counterparties'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleCounterpartyTest(TestCase):
    """ Test module for updating an existing counterparty record """

    def setUp(self):
        self.counterparty1 = Counterparty.objects.create(name='Контрагент1', rating='BB-')
        self.counterparty2 = Counterparty.objects.create(name='Контрагент2', rating='CCC')
        self.valid_payload = {'name': 'Контрагент1', 'rating': 'BB'}
        self.invalid_payload = {'name': '', 'rating': 'CCC'}

    def test_valid_update_counterparty(self):
        response = client.put(
            reverse('get_delete_update_counterparty', kwargs={'id': self.counterparty1.id}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_counterparty(self):
        response = client.put(
            reverse('get_delete_update_counterparty', kwargs={'id': self.counterparty1.id}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleCounterpartyTest(TestCase):
    """ Test module for deleting an existing counterparty record """

    def setUp(self):
        self.counterparty1 = Counterparty.objects.create(name='Контрагент1', rating='CCC')
        self.counterparty2 = Counterparty.objects.create(name='Контрагент2', rating='BB-')

    def test_valid_delete_counterparty(self):
        response = client.delete(
            reverse('get_delete_update_counterparty', kwargs={'id': self.counterparty2.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_delete_counterparty(self):
        response = client.delete(
            reverse('get_delete_update_counterparty', kwargs={'id': 9999999999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
