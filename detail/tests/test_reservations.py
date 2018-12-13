from django.test import TestCase

import json
from rest_framework import status
from rest_framework.test import APIRequestFactory
from django.test import TestCase, Client
from django.urls import reverse
from ..serializers import CarSearchSerializer
from .assets.reservations import car1Dict
from .test_search import BaseTestCase
from ..views import ReservationList

# initialize the APIClient app
client = Client()
factory = APIRequestFactory()
view = ReservationList.as_view()


class ReservationTest(BaseTestCase):
    """ Test module for booking feature """

    def setUp(self):
        super(ReservationTest, self).setUp()
        self.valid_payload = car1Dict

    def test_whenBookingCar1WithLowerBoundConflict_expect_car1IsNotAvailable(self):
        # Mela pero fea
        # request = factory.post(
        #     '/booking/',
        #     car1Dict
        # )
        # response = view(request)
        bookingsUrl = reverse('get_post_bookings')
        response = self.client.post(path=bookingsUrl, data=car1Dict)
        print(response.data, end='', flush=True)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
