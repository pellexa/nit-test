from django.db import models
from django.core.exceptions import ValidationError
from deliverypoints.models import DeliveryPoint
from counterparties.models import Counterparty

class Deal(models.Model):
    type = models.CharField(max_length=255, blank=False)
    dateDeal = models.DateTimeField(blank=False)
    deliveryPoint = models.ForeignKey(DeliveryPoint, on_delete=models.PROTECT, blank=False, related_name='list_deliveryPoints')
    volume = models.IntegerField(blank=False)
    price = models.DecimalField(max_digits=20, decimal_places=3, blank=False)
    deliveryStart = models.DateTimeField(blank=False)
    deliveryEnd = models.DateTimeField(blank=False)
    tool = models.CharField(max_length=255, blank=False)
    counterparty = models.ForeignKey(Counterparty, on_delete=models.PROTECT, blank=False, related_name='list_counterparties')

    class Meta:
        unique_together = ('type', 'dateDeal', 'deliveryPoint', 'deliveryStart', 'deliveryEnd', 'tool', 'counterparty')
