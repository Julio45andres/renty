from ...models import Car

token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjkwOTBjZGI5MmIzOTZiNTQyM2JhYjYyOWM5ZTk4MmFkYzIxYmQxMTIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vcmVudHktdnVlIiwiYXVkIjoicmVudHktdnVlIiwiYXV0aF90aW1lIjoxNTQ0NjgyOTEzLCJ1c2VyX2lkIjoiTERGaTVaZ2VSYWdCVGEzQWlHTWZKbEl4WmdkMiIsInN1YiI6IkxERmk1WmdlUmFnQlRhM0FpR01mSmxJeFpnZDIiLCJpYXQiOjE1NDQ2ODI5MTMsImV4cCI6MTU0NDY4NjUxMywiZW1haWwiOiJqdWxpYW4ubXVub3ptQHVkZWEuZWR1LmNvIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbImp1bGlhbi5tdW5vem1AdWRlYS5lZHUuY28iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.KYizls1J3NY_kD3zokbEaFcznlelXD1TvHc8tL4AAGPpdU7YVxQ_6smKGjK2jTw7LrBB1nS4s182ptg_JicsbJGPF9i4YWyArp9q5d4fTRr0i_2V-bRHE5-7ySeW7-EcpNH4XJR9_3-vMzK9hEh61K933lVKmW4bCgncUcvQKBEJOVOuvMnWQX7Qd9a6te5ow4an6d3BZMPGTPbEHuNla60NgmDADIEfL0ti2q4F5FP8vXsyGFOpQh6xQB3XbmNzg2-NxLOh_kzkdbX4ND3bSw5xKEQYwWpJDUzkK0kzwb4ysgEI2CLFhfYnGiixjztqVnq03ArOUhV_QMD-8QXU7Q'


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
