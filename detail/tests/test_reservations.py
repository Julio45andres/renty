from django.test import TestCase

import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..serializers import CarSearchSerializer
from .assets.reservations import car1Dict
from .test_search import BaseTestCase

# initialize the APIClient app
client = Client()


class ReservationTest(BaseTestCase):
    """ Test module for booking feature """

    def setUp(self):
        super(ReservationTest, self).setUp()
        self.valid_payload = car1Dict

    def test_whenBookingCar1WithLowerBoundConflict_expect_car1IsNotAvailable(self):
        response = client.post(
            reverse('get_post_bookings'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        print(response.data, end='', flush=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
