from django.db import transaction
from django.test import TestCase
from pint import DimensionalityError

from pintunitfield import ureg
from tests.dummyapp.models import Product


class TestFieldSave(TestCase):

    def test_stores_unit(self):
        with transaction.atomic():
            Product.objects.create(name='Rice', amount=1, unit="gram")
            item = Product.objects.get(name='Rice')
            self.assertEqual(item.unit, ureg.gram)

    def test_no_unit_provided(self):
        with transaction.atomic():
            Product.objects.create(name='Eggs', amount=12)
            item = Product.objects.get(name='Eggs')
            self.assertEqual(item.unit, ureg.count)
