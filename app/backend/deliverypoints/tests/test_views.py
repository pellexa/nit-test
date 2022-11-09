import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import DeliveryPoint
from ..serializers import DeliveryPointSerializer

# initialize the APIClient app
client = Client()

class GetAllDeliveryPointsTest(TestCase):
    """ Test module for GET all deliveryPoints API """

    def setUp(self):
        self.deliveryPoint1 = DeliveryPoint.objects.create(name='VIP Bereg')
        self.deliveryPoint2 = DeliveryPoint.objects.create(name='VTP Austria')
        self.deliveryPoint3 = DeliveryPoint.objects.create(name='Olbernhau II')
        self.deliveryPoint4 = DeliveryPoint.objects.create(name='Baumgarten')

    def test_get_all_deliveryPoints(self):
        # get API response
        response = client.get(reverse('get_post_deliveryPoints'))
        # get data from db
        deliveryPoints = DeliveryPoint.objects.all()
        serializer = DeliveryPointSerializer(deliveryPoints, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_deliveryPoint(self):
        response = client.get(
            reverse('get_delete_update_deliveryPoint', kwargs={'id': self.deliveryPoint1.id}))
        deliveryPoint = DeliveryPoint.objects.get(id=self.deliveryPoint1.id)
        serializer = DeliveryPointSerializer(deliveryPoint)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_deliveryPoint(self):
        response = client.get(
            reverse('get_delete_update_deliveryPoint', kwargs={'id': 9999999999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewСounterpartyTest(TestCase):
    """ Test module for inserting a new deliveryPoint """

    def setUp(self):
        self.valid_payload = {'name': 'Baumgarten'}
        self.invalid_payload = {'name': ''}

    def test_create_valid_deliveryPoint(self):
        response = client.post(
            reverse('get_post_deliveryPoints'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_deliveryPoint(self):
        response = client.post(
            reverse('get_post_deliveryPoints'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleDeliveryPointTest(TestCase):
    """ Test module for updating an existing deliveryPoint record """

    def setUp(self):
        self.deliveryPoint1 = DeliveryPoint.objects.create(name='Olbernhau I')
        self.deliveryPoint2 = DeliveryPoint.objects.create(name='Baumgarten')
        self.valid_payload = {'name': 'Olbernhau II'}
        self.invalid_payload = {'name': ''}

    def test_valid_update_deliveryPoint(self):
        response = client.put(
            reverse('get_delete_update_deliveryPoint', kwargs={'id': self.deliveryPoint1.id}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_deliveryPoint(self):
        response = client.put(
            reverse('get_delete_update_deliveryPoint', kwargs={'id': self.deliveryPoint1.id}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleDeliveryPointTest(TestCase):
    """ Test module for deleting an existing deliveryPoint record """

    def setUp(self):
        self.deliveryPoint1 = DeliveryPoint.objects.create(name='Baumgarten')
        self.deliveryPoint2 = DeliveryPoint.objects.create(name='Olbernhau II')

    def test_valid_delete_deliveryPoint(self):
        response = client.delete(
            reverse('get_delete_update_deliveryPoint', kwargs={'id': self.deliveryPoint2.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_delete_deliveryPoint(self):
        response = client.delete(
            reverse('get_delete_update_deliveryPoint', kwargs={'id': 9999999999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
