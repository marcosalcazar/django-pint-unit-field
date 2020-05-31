from django.db import models

from pintunitfield.fields import PintUnitField


class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    unit = PintUnitField()
