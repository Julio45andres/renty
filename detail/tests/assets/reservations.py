from ...models import Car

token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjkwOTBjZGI5MmIzOTZiNTQyM2JhYjYyOWM5ZTk4MmFkYzIxYmQxMTIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vcmVudHktdnVlIiwiYXVkIjoicmVudHktdnVlIiwiYXV0aF90aW1lIjoxNTQ0NjgzNzQyLCJ1c2VyX2lkIjoiTERGaTVaZ2VSYWdCVGEzQWlHTWZKbEl4WmdkMiIsInN1YiI6IkxERmk1WmdlUmFnQlRhM0FpR01mSmxJeFpnZDIiLCJpYXQiOjE1NDQ2ODM3NDIsImV4cCI6MTU0NDY4NzM0MiwiZW1haWwiOiJqdWxpYW4ubXVub3ptQHVkZWEuZWR1LmNvIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbImp1bGlhbi5tdW5vem1AdWRlYS5lZHUuY28iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.BYaXgmp1y0pzXWHSUa-TWt_HzUyt0ahyqgeTH8dpOD4moMlTN1pQhQvjG-ZI3jQOIH8zbNzKHYhHm5lRRrStxlx9Ee_xMZ1V-XLWPxZCGtJVd9mqfa7aNdp94Vqi68mbUcP4g1SGMy1jr5HLvI0zIIyJuf29cu7wfkocptcH5wzRhGsdyMuRTTCiLTyka2Gck6XRjMjlX048NGNpzhDM5KUa_QnLCet926a5RIVEe_uAbrB7ziTFkGFfb9nLucBeHtaBanOP3Rqz-khVMtUgj6Ht57ZrG33yEalOdjD3Pz_l6Nn0yZ3sLecYURiT0qIdLphIgHnEDjer9IGLsZTaew'


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
