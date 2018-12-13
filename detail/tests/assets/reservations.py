from ...models import Car

token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjkwOTBjZGI5MmIzOTZiNTQyM2JhYjYyOWM5ZTk4MmFkYzIxYmQxMTIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vcmVudHktdnVlIiwiYXVkIjoicmVudHktdnVlIiwiYXV0aF90aW1lIjoxNTQ0Njg0NDMyLCJ1c2VyX2lkIjoiTERGaTVaZ2VSYWdCVGEzQWlHTWZKbEl4WmdkMiIsInN1YiI6IkxERmk1WmdlUmFnQlRhM0FpR01mSmxJeFpnZDIiLCJpYXQiOjE1NDQ2ODQ0MzIsImV4cCI6MTU0NDY4ODAzMiwiZW1haWwiOiJqdWxpYW4ubXVub3ptQHVkZWEuZWR1LmNvIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbImp1bGlhbi5tdW5vem1AdWRlYS5lZHUuY28iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.GIKqKliasfnuS9AjZTiulY5LZzg57Wj70m286cvqw9mgFtkjik5Kkgvni4cJZzby_JNQVhquyzn987KejCGaiETDXmGLGUVlpNVkZH3Hz5lxbFmAN2YnM93TruE-kt--lXe3LqoxuLKGnZb0X91BCvF2FpqwBJoJ0_J-3dUBXfqxAQUxXt6r7oowCd4VgOu-AEMnLizTd6M3QXVBKvbIRksJ0rfJF2JQd5g-uZ9zgrqCdqr0BBBlSx7ys8v7pYqjnQ1TRQXZdOKctFguBxNGacfKoYfXmTWRqHf3aWksRAmCvDPf4tfwaJCQjkkrvekWe2SA-_0IDUocZqaA1cCZaQ'


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
