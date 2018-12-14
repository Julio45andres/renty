from ...models import Car

token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjkwOTBjZGI5MmIzOTZiNTQyM2JhYjYyOWM5ZTk4MmFkYzIxYmQxMTIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vcmVudHktdnVlIiwiYXVkIjoicmVudHktdnVlIiwiYXV0aF90aW1lIjoxNTQ0NzYzNjE3LCJ1c2VyX2lkIjoiTERGaTVaZ2VSYWdCVGEzQWlHTWZKbEl4WmdkMiIsInN1YiI6IkxERmk1WmdlUmFnQlRhM0FpR01mSmxJeFpnZDIiLCJpYXQiOjE1NDQ3NjM2MTcsImV4cCI6MTU0NDc2NzIxNywiZW1haWwiOiJqdWxpYW4ubXVub3ptQHVkZWEuZWR1LmNvIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbImp1bGlhbi5tdW5vem1AdWRlYS5lZHUuY28iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.ZQD-Vdv2UoFpkwcrh756U178ta0yfZFA2ofvxCUFrsQ8Pra_OH6UxbpzCi2qr6eEx9CxinhGV-YakfTtTpRrjW0BsE1-Cg61VmRoWNMjeQyy5cWoRudEjZ7ozw8HaOC7UFuhe5chZhVbbz3rV7qvIViBiDx83rh_BT_lXyEsC09Xxn5mw_v0Gt2mkxMgWJY8IkVS4ZlFQDfHnfW-aqc5gaGgIfhAHt54SW0Dr7lEb6zecijzQBwkFxl_XBvikcOU-TTaeIN6n2yFOCeyGoDYrzTOI4lwivp9BERWwtI3_UrE371FKQCrWgkaHfHrtuNlz0YcwX2KTpnI0esNqwidaA'


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
            "deliverPlace": "MDE",
            "deliverDate": to
        }
        return car1Request
# from "2018-10-13"
# to "2018-10-15"
