from ...models import Car

token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjkwOTBjZGI5MmIzOTZiNTQyM2JhYjYyOWM5ZTk4MmFkYzIxYmQxMTIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vcmVudHktdnVlIiwiYXVkIjoicmVudHktdnVlIiwiYXV0aF90aW1lIjoxNTQ0NzY0Mjk2LCJ1c2VyX2lkIjoiTERGaTVaZ2VSYWdCVGEzQWlHTWZKbEl4WmdkMiIsInN1YiI6IkxERmk1WmdlUmFnQlRhM0FpR01mSmxJeFpnZDIiLCJpYXQiOjE1NDQ3NjQyOTYsImV4cCI6MTU0NDc2Nzg5NiwiZW1haWwiOiJqdWxpYW4ubXVub3ptQHVkZWEuZWR1LmNvIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbImp1bGlhbi5tdW5vem1AdWRlYS5lZHUuY28iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.dCL6NZ-SakpMQWOEBHjfiF00WstLYPgbaWZ8fbedwk0IrNCdgFkwfq99od-kbokYWnHszdBvkN0-A_anDa7JRgp-qM1NVHv3WzNzg2HzI6FOr1oQ3FTd9d_XUygvJnDWQHuSJXaS-tg07FyfUG8r_TAV2YT5kdwam8-SIKAkapjeNa_vYy198wz5jMkGjR-OtJFCq3WA9QpAUTR81fOtryy4gOdR74dBHJ_y9UnjsX-qWI_eK_PdWcg8TF0kf0hhDkEfYF_KrQVZCy79L-tK5R0jHLXdUYsVpE8FKbj7aiwAVZv11P4agFf6Xb_KSpDY6cEfzOvMv4I_REjrp6ppqg'


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
