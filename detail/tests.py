from django.test import TestCase

# Create your tests here.
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import CarRent, Car, CarRental
from .serializers import CarSearchSerializer

from django.utils.dateparse import parse_datetime, parse_date
from datetime import datetime, date

# initialize the APIClient app
client = Client()


class BookingTest(TestCase):
    """ Test module for booking model """

    def setUp(self):
        rental = CarRental.objects.create(_id=1, name="f")
        car1 = Car.objects.create(brand="ff", thumbnail="ff", price=3, category="SUV",
                                  model="2019", pickup="Aeropuerto", rental=rental, plate=23, rating=3, capacity=4, transmission="Mecanica", doors=5, color="Azul", kms=1)
        car2 = Car.objects.create(brand="ff", thumbnail="ff", price=3, category="SUV",
                                  model="2019", pickup="Aeropuerto", rental=rental, plate=11, rating=3, capacity=4, transmission="Mecanica", doors=5, color="Azul", kms=1)
        CarRent.objects.create(car=car1, token="eREw", uidUser=45, bookingDate=_parse_date("2018-11-23"), pickup="Aeropuerto",
                               pickupDate=_parse_date("2018-11-25"), deliverPlace="Parque del poblado", deliverDate=_parse_date("2018-11-27"), rental=rental)
        CarRent.objects.create(
            car=car2,
            token="4fR",
            uidUser=32,
            bookingDate=_parse_date("2018-11-27"),
            pickup="Aeropuerto",
            pickupDate=_parse_date("2018-11-28"),
            deliverPlace="Parque del poblado",
            deliverDate=_parse_date("2018-11-30"),
            rental=rental
        )

    def test_booking_availability(self):
        # get API response
        # response = client.get(reverse('car-search', kwargs={
        #     'from': _parse_date("2018-11-24"), 'to': _parse_date("2018-11-26")
        # }))
        response = client.get(
            "%s?from=2018-11-24&to=2018-11-26" % reverse('car-search'))
        serializedCar2 = CarSearchSerializer(
            Car.objects.filter(plate=11), many=True)
        self.assertEqual(response.data, serializedCar2.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


def _parse_date(date):
    parsed_date = parse_date(date)
    return parsed_date
