from rest_framework import serializers
from .models import Deal

class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ('id', 'type', 'dateDeal', 'deliveryPoint', 'volume', 'price', 'deliveryStart', 'deliveryEnd', 'tool', 'counterparty')
