import json

from rest_framework import status
from django.test import Client
from django.urls import reverse
from ..models import Car
from ..serializers import CarSearchSerializer

from .BaseTestCase import BaseTestCase
from .assets.dates import _parse_date

# initialize the APIClient app
client = Client()


class SearchTest(BaseTestCase):
    """ Test module for search feature """

    def setUp(self):
        """ Por legibilidad y mantenibilidad tenemos todo el septup inicial 
            en un test case base llamado BaseTestCase """
        super(SearchTest, self).setUp()
        """ car 1 info 
                id: 1
                pickup date: 2018-11-25,
                deliver date: 2018-11-27
            car 2 info
                id: 2
                pickup date: 2018-11-28
                deliver date: 2018-12-5 """

    def test_whenSearchingCar1WithLowerBoundConflict_expect_car1IsNotAvailable(self):
        # GET API response
        response = client.get(
            "%s?from=2018-11-24&to=2018-11-26" % reverse('car-search'))
        # solamente el auto 2 esta disponible
        serializedCar2 = CarSearchSerializer(
            Car.objects.filter(plate=2), many=True)
        self.assertEqual(response.data, serializedCar2.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_whenSearchingCar2WithUpperBoundConflict_expect_car2IsNotAvailable(self):
        # GET API response
        response = client.get(
            "%s?from=2018-12-3&to=2018-12-7" % reverse('car-search'))
        # solamente el auto 1 está disponible
        serializedCar1 = CarSearchSerializer(
            Car.objects.filter(plate=1), many=True)
        self.assertEqual(response.data, serializedCar1.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_whenSearchingCar2InBetweenAReservation_expect_car2IsNotAvailable(self):
        # GET API response
        response = client.get(
            "%s?from=2018-11-30&to=2018-12-2" % reverse('car-search'))
        # solamente el auto 1 está disponible
        serializedCar1 = CarSearchSerializer(
            Car.objects.filter(plate=1), many=True)
        self.assertEqual(response.data, serializedCar1.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_whenSearchingDatesWithNoReservations_expect_allCarsAreAvailable(self):
        # GET API response
        response = client.get(
            "%s?from=2018-10-1&to=2018-10-5" % reverse('car-search'))
        # solamente el auto 1 está disponible
        serializedCar1 = CarSearchSerializer(
            Car.objects.all(), many=True)
        self.assertEqual(response.data, serializedCar1.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
