from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from .models import CarRental, Car, CarRent
from .serializers import RentalSerializer, CarSerializer, CarSerializerToSave, CarSearchSerializer, ReservationSerializer, DeleteReservationSerializer
from django.http import Http404, HttpResponse
from django.utils.dateparse import parse_datetime, parse_date
from datetime import datetime, date
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
import firebase_admin
from firebase_admin import credentials, auth

class RentalView(generics.ListAPIView):
    serializer_class = RentalSerializer

    def get_queryset(self):
        queryset = CarRental.objects.all()
        return queryset

    def post(self, request):
        serializer = RentalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@require_http_methods(["GET", "POST"])
def api_getto(request):
    response = JsonResponse(
        # your stuff here
    )
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response


class CarView(APIView):
    serializer_class = CarSerializer

    def get(self, request, carid, format=None):
        if carid is not None:
            cars = Car.objects.filter(id=carid)
            serializer = CarSerializer(cars[0], many=False)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

import os.path

class CarSearchView(generics.ListAPIView):
    serializer_class = CarSearchSerializer

    def get_queryset(self):
        queryset = Car.objects.all()
        reservatedCars = CarRent.objects.all()
        # type es una palabra reservada de python
        _type = self.request.query_params.get('type', None)
        pickup = self.request.query_params.get('pickup', None)
        if _type is not None:
            queryset = queryset.filter(category__iexact=_type)
        if pickup is not None:
            queryset = queryset.filter(pickup__iexact=pickup)
        _from = self.request.query_params.get('from', None)
        _from = _parse_date(str(_from))
        to = self.request.query_params.get('to', None)
        to = _parse_date(str(to))
        if _from is None or to is None:
            queryset = Car.objects.none()
        else:
            if _from > to:
                raise Http404
            fromReservations = reservatedCars.filter(
                pickupDate__range=(_from, to))
            toReservations = reservatedCars.filter(
                deliverDate__range=(_from, to))
            # Union
            reservatedCars = (fromReservations | toReservations).values('car')
            queryset = queryset.exclude(id__in=reservatedCars)
        return queryset


def _parse_date(date):
    parsed_date = parse_date(date)
    return parsed_date



class ReservationList(generics.ListCreateAPIView):
    my_path = os.path.abspath(os.path.dirname(__file__))
    cred = credentials.Certificate(os.path.join(
        my_path, "../renty-python-firebase-adminsdk.json"))
    default_app = firebase_admin.initialize_app(cred)
    serializer_class = ReservationSerializer
    lookup_url_kwarg="token"

    def get_queryset(self):
        token = self.kwargs.get(self.lookup_url_kwarg)
        print("token: "+token)
        rents = CarRent.objects.all()
        if token is not None:
            uidUser = takeUid(token)
            if uidUser is not None:
                #filtra las reservas del usuario
                rents = rents.filter(uidUser=uidUser)
                #filtra las reservas activas
                rents = rents.filter(token="activo")
                return rents
            else:
                print("Token invalido")
        else:
            print("token none")
        

    def post(self, request):
        # se obtiene la información del usuario
        token = request.POST.get('token')
        uidUser = takeUid(token)
        if uidUser is None :
            error = {
                "error": "Token invalido"
            }
            return Response(error, status=status.HTTP_401_UNAUTHORIZED)

        print("uidUser: "+uidUser)
        # se obtiene la información del auto a rentar
        cars = Car.objects.filter(id=request.POST.get('carId'))
        car = cars[0]
        # se obitene la información de la empresa rentadora del auto
        rental = car.rental
        # se obtiene el resto de información
        # Fecha en la que se hizo la reserva
        bookingDate = request.POST.get('bookingDate')
        bookingDate = _parse_date(str(bookingDate))
        # pickup
        pickup = request.POST.get('pickup')
        # fecha en la que se recoge el auto -comienza la renta-
        pickupDate = request.POST.get('pickupDate')
        pickupDate = _parse_date(str(pickupDate))
        # Lugar donde se entregará el auto cuando finalice la renta
        deliverPlace = request.POST.get('deliverPlace')
        # fecha en la que se entrega el auto -fin de la renta-
        deliverDate = request.POST.get('deliverDate')
        deliverDate = _parse_date(str(deliverDate))

        # se crea el objeto a guardar
        print("A guardar en base de datos")
        booking = CarRent(
            car=car,
            token="activo",
            uidUser=uidUser,
            bookingDate=bookingDate,
            pickup=pickup,
            pickupDate=pickupDate,
            deliverPlace=deliverPlace,
            deliverDate=deliverDate,
            rental=rental
        )
        print("Se gurdó en la base de datos")
        #se guarda el objeto
        #booking.save()
        try:
            booking.save()
            print(booking.id)
            if booking.id is not None:
                data = {
                    "statusCode":200
                }
                return Response(data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            data = {
                "error": str(e)
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
    # delete an object and send a confirmation response
        token = request.POST.get('token')
        print("token: "+token)
        uidUser = takeUid(token)
        if uidUser is not None:
            #se elimina el dato
            print("uidUSer: "+uidUser)
            try:
                bookingId = request.POST.get('bookingId')
                booking = CarRent.objects.get(id=bookingId)
                if booking.token == "cancelado":
                    error = {
                        "error": "La reserva ya se ha cancelado con anterioridad"
                    }
                    return Response(error, status=status.HTTP_400_BAD_REQUEST) 
                booking.token = "cancelado"
                booking.save()
                data = {
                    "mensaje":"Se ha cancelado la reserva"
                }
                serializer_context = {
                    'request': request,
                }
                serializer = DeleteReservationSerializer(CarRent.objects.all(), context=serializer_context)
                return Response(data)
            except ValueError as a:
                print(a)
                error:{
                    "error":a
                }
                return Response(error, status=status.HTTP_400_BAD_REQUEST) 
        else:
            error={
                "error":"Token invalido"
            }
            return Response(error, status=status.HTTP_400_BAD_REQUEST)


def takeUid(token):
    try:
        decoded_token = auth.verify_id_token(token)
        uid = decoded_token['uid']
        return uid
    except ValueError as a:
        print(a)
        return None