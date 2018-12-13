from ...models import Car

token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjkwOTBjZGI5MmIzOTZiNTQyM2JhYjYyOWM5ZTk4MmFkYzIxYmQxMTIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vcmVudHktdnVlIiwiYXVkIjoicmVudHktdnVlIiwiYXV0aF90aW1lIjoxNTQ0NjgyNTE1LCJ1c2VyX2lkIjoiTERGaTVaZ2VSYWdCVGEzQWlHTWZKbEl4WmdkMiIsInN1YiI6IkxERmk1WmdlUmFnQlRhM0FpR01mSmxJeFpnZDIiLCJpYXQiOjE1NDQ2ODI1MTUsImV4cCI6MTU0NDY4NjExNSwiZW1haWwiOiJqdWxpYW4ubXVub3ptQHVkZWEuZWR1LmNvIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbImp1bGlhbi5tdW5vem1AdWRlYS5lZHUuY28iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.lkhBbNouUo7b1GdhLsULKxNaVbImTiobKjPDyFzbB9pKCGtLW0cmRLR_97iPdJqFq0A7e7hbQ-p4xGZiA2kb8TjxGp-qqCWaYuvFPp74EH_7KZBg9zLn9f9xOJUHbHlFxh9xTeEdmFEWuJNtnw3ky1SHaNVU_LmxVfXY5nsbgF-3noFYMsx92JIDgod1Y9R0-FPFnOZrW4rC4Acoq2YMUrbQD7lfsLmn8BCJkyzFl2HpFRKGPDGgV8GecTWbqi2d4qLJiUiim8ywK4ML44eK8QvjVvOgDMYgpF1UkTBA3Q91FmeOv0IagFtEQMag3JSLu8_7HrAUuMkQY87Iw_MlDA'


class RequestBuilder:
    def build(_from, to, car=None):
        """ En los métodos setup se generan nuevos autos cada vez que corre un test, sin embargo
            la tabla autos tiene un id autoincrementable, por lo cual los nuevos autos no empiezan desde 1.
            Es válido que un auto con id 7 sea el primero en la base de datos, pues los autos
            con id del 1 al 6 han sido borrados despues de algunos tests, por esta razon buscamos al primero
            y no por id específico. """
        if car is None:
            car = Car.objects.first()
        id = car.id
        car1Request = {
            'token': token,
            "carId": id,
            "bookingDate": "2018-11-12",
            "pickup": "MDE",
            "pickupDate": _from,
            "deliverPlace": to,
            "deliverDate": "2018-10-15"
        }
        return car1Request
# from "2018-10-13"
# to "2018-10-15"
