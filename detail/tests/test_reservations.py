import json

from rest_framework import status
from django.test import Client
from django.urls import reverse
from ..models import Car
from ..serializers import CarSearchSerializer
from .assets.reservations import RequestBuilder
from .BaseTestCase import BaseTestCase

# initialize the APIClient app
client = Client()

""" Test case for ReservationList view """


class ReservationTest(BaseTestCase):
    """ Test module for booking feature """

    def setUp(self):
        """ Por legibilidad y mantenibilidad tenemos todo el septup inicial 
            en un test case base llamado BaseTestCase
            los términos booking y reservation se usan de manera intercambiable. """
        super(ReservationTest, self).setUp()
        """ car 1 info 
                id: 1
                pickup date: 2018-11-25,
                deliver date: 2018-11-27
            car 2 info
                id: 2
                pickup date: 2018-11-28
                deliver date: 2018-12-5 """

    # def test_whenBookingCar1WithoutConflict_expect_car1IsAvailable(self):
    #     # POST api response
    #     request = RequestBuilder.build(
    #         _from='2018-10-25', to='2018-10-27')
    #     bookingsUrl = reverse('get_post_bookings')
    #     response = client.post(
    #         path=bookingsUrl, data=request)
    #     # print(Car.objects.all())
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_whenBookingCar1WithLowerBound_expect_car1IsNotAvailable(self):
        # POST api response
        # Some booking
        aBooking = RequestBuilder.build(
            _from='2018-11-25', to='2018-11-27')
        bookingsUrl = reverse('get_post_bookings')
        response = client.post(
            path=bookingsUrl, data=aBooking)
        # The same car
        sameCar = Car.objects.first()
        # a booking with conflicting lower bounds on dates
        conflictingResquest = RequestBuilder.build(
            _from='2018-11-24', to='2018-11-26', car=sameCar)
        response = client.post(
            path=bookingsUrl, data=conflictingResquest)
        print(Car.objects.all())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
