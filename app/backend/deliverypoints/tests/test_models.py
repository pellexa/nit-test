from django.test import TestCase
from ..models import DeliveryPoint

class DeliveryPointTest(TestCase):
    """ Test module for DeliveryPoint model """

    def setUp(self):
        DeliveryPoint.objects.create(name='VIP Bereg')
        DeliveryPoint.objects.create(name='VTP Austria') 

    def test_deliveryPoint(self):
        deliveryPoint1 = DeliveryPoint.objects.get(name='VIP Bereg')
        deliveryPoint2 = DeliveryPoint.objects.get(name='VTP Austria')
        self.assertNotEqual(deliveryPoint1, deliveryPoint2)
