from rest_framework import serializers
from .models import DeliveryPoint

class DeliveryPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPoint
        fields = ('id', 'name')
