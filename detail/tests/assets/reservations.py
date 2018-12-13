from ...models import Car

token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjkwOTBjZGI5MmIzOTZiNTQyM2JhYjYyOWM5ZTk4MmFkYzIxYmQxMTIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vcmVudHktdnVlIiwiYXVkIjoicmVudHktdnVlIiwiYXV0aF90aW1lIjoxNTQ0NzI2OTgzLCJ1c2VyX2lkIjoiTERGaTVaZ2VSYWdCVGEzQWlHTWZKbEl4WmdkMiIsInN1YiI6IkxERmk1WmdlUmFnQlRhM0FpR01mSmxJeFpnZDIiLCJpYXQiOjE1NDQ3MjY5ODMsImV4cCI6MTU0NDczMDU4MywiZW1haWwiOiJqdWxpYW4ubXVub3ptQHVkZWEuZWR1LmNvIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbImp1bGlhbi5tdW5vem1AdWRlYS5lZHUuY28iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.dlM9EC1TjAlprRZZRnjc7HiOkI05XL0eSzMPhbmxW0DqNBbMqtyNFg8aZcQhI7H6I9JfoW1rEQMjbibeuwVkNYZ6f86TcrL5ucrYq0gRo67C1RbqYW4_NgdwJgsW4Hg_zq07oN7dJwjSbbH1nyUid83mYTqqxgCASYHogE8E-glwh-tKiJ7lYYcetGxABaX3CD_C0vb6KZxRAoXH9vP1nZLk09RqKb2m3ShteKuh6ENU-ecsPLzhVo-DJfZr1m0B_z7Iu8Q5CepfvdBeSk8GDwXu0mtBACqTdkClhUMQmGyJdhG-MuQ5Jmixabg6jx1lZIy7x01sANju2bW_3iT6LA'


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
