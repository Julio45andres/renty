from django.test import TestCase

from django.test import TestCase
from ..models import CarRent, Car, CarRental

from .assets.dates import _parse_date


class BaseTestCase(TestCase):
    """ Test module for search feature """

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
