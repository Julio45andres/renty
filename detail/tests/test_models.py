# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from ..models import CarRent, Car, CarRental

from .assets.dates import _parse_date


class ModelsTest(TestCase):
    def test_models(self):
        carRental = CarRental.objects.create(_id=887, name='jaja')
        self.assertEqual(carRental._id, 887)
        self.assertEqual(carRental.name, 'jaja')
