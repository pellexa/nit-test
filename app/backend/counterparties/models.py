from django.db import models

class Counterparty(models.Model):
    name = models.CharField(max_length=255, unique=True)
    rating = models.CharField( max_length=255)

