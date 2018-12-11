from django.test import TestCase

# Create your tests here.
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import CarRent, Car, CarRental
from ..serializers import CarSearchSerializer

from django.utils.dateparse import parse_datetime, parse_date
from datetime import datetime, date

# initialize the APIClient app
client = Client()


class SearchTest(TestCase):
    """ Test module for booking model """

    def setUp(self):
        pictures = ["https://c1.staticflickr.com/9/8728/16671205057_889930d3c0_b.jpg",
                    "http://www.mansory.com/files/styles/mansory_range_overview_main/public/media/cars/bugatti_veyron_16.4/linea_vivere/MANSORY_vivere_ext_06.jpg?itok=oDKbqzwI"]
        rental = CarRental.objects.create(_id=1, name="f")
        car1 = Car.objects.create(brand="Chevrolet", thumbnail="ff", price=3, category="SUV",
                                  model="2019", pickup="Aeropuerto", rental=rental, plate=1, rating=3, capacity=4,
                                  transmission="Mecanica", doors=5, color="Azul", kms=1, pictures=pictures)
        car2 = Car.objects.create(brand="Bugatti", thumbnail="ff", price=3, category="SUV",
                                  model="2019", pickup="Aeropuerto", rental=rental, plate=2, rating=3, capacity=4,
                                  transmission="Mecanica", doors=5, color="Azul", kms=1, pictures=pictures)
        CarRent.objects.create(car=car1, token="eREw", uidUser=45, bookingDate=_parse_date("2018-11-23"), pickup="Aeropuerto",
                               pickupDate=_parse_date("2018-11-25"), deliverPlace="Parque del poblado",
                               deliverDate=_parse_date("2018-11-27"), rental=rental)
        CarRent.objects.create(
            car=car2,
            token="4fR",
            uidUser=32,
            bookingDate=_parse_date("2018-11-27"),
            pickup="Aeropuerto",
            pickupDate=_parse_date("2018-11-28"),
            deliverPlace="Parque del poblado",
            deliverDate=_parse_date("2018-12-5"),
            rental=rental
        )

    def test_whenSearchingCar1WithLowerBoundConflict_expect_car1IsNotAvailable(self):
        # get API response
        response = client.get(
            "%s?from=2018-11-24&to=2018-11-26" % reverse('car-search'))
        # Only car 2 is available
        serializedCar2 = CarSearchSerializer(
            Car.objects.filter(plate=2), many=True)
        self.assertEqual(response.data, serializedCar2.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_whenSearchingCar2WithUpperBoundConflict_expect_car2IsNotAvailable(self):
        # get API response
        response = client.get(
            "%s?from=2018-12-3&to=2018-12-7" % reverse('car-search'))
        # Only car 1 is available
        serializedCar1 = CarSearchSerializer(
            Car.objects.filter(plate=1), many=True)
        self.assertEqual(response.data, serializedCar1.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_whenSearchingCar2InBetweenAReservation_expect_car2IsNotAvailable(self):
        # get API response
        response = client.get(
            "%s?from=2018-11-30&to=2018-12-2" % reverse('car-search'))
        # Only car 1 is available
        serializedCar1 = CarSearchSerializer(
            Car.objects.filter(plate=1), many=True)
        self.assertEqual(response.data, serializedCar1.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_whenSearchingDatesWithNoReservations_expect_allCarsAreAvailable(self):
        # get API response
        response = client.get(
            "%s?from=2018-10-1&to=2018-10-5" % reverse('car-search'))
        # Only car 1 is available
        serializedCar1 = CarSearchSerializer(
            Car.objects.all(), many=True)
        self.assertEqual(response.data, serializedCar1.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


def _parse_date(date):
    parsed_date = parse_date(date)
    return parsed_date
