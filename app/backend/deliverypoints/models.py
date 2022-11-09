from django.db import models

class DeliveryPoint(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
