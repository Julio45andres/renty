from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from .models import CarRental, Car, CarRent
from .serializers import RentalSerializer, CarSerializer, CarSerializerToSave, CarSearchSerializer, ReservationSerializer
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


'''
    def post(self, request):
        serializer = CarSerializerToSave(data=request.data)
        if serializer.is_valid():
            serializer.save()
            Response["Access-Control-Allow-Origin"] = "*"
            Response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
            Response["Access-Control-Max-Age"] = "1000"
            Response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
import os.path


class ReservationView(APIView):
    serializer_class = RentalSerializer
    my_path = os.path.abspath(os.path.dirname(__file__))
    cred = credentials.Certificate(os.path.join(
        my_path, "../renty-python-firebase-adminsdk.json"))
    default_app = firebase_admin.initialize_app(cred)

    def get(self, request):
        try:
            token = self.request.query_params.get('tokenId', None)
            if token is not None:
                decoded_token = auth.verify_id_token(token)
                uid = decoded_token['uid']
                data = {
                    "uid": uid
                }
                return Response(data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            data = {
                "error": str(e)
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)


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
            betweenReservations = reservatedCars.filter(
                pickupDate__lte=_from,
                deliverDate__gte=to
            )
            # Union
            reservatedCars = (fromReservations | toReservations |
                              betweenReservations).values('car')
            queryset = queryset.exclude(id__in=reservatedCars)
        return queryset


def _parse_date(date):
    parsed_date = parse_date(date)
    return parsed_date


class ReservationList(generics.ListCreateAPIView):
    serializer_class = ReservationSerializer

    def get(self, request):
        def message():
            text = "hola mundo"
        return Response("hola mundo")

    def post(self, request):
        # print("Request: "+ request.data)
        # se obtiene la información
        # información del usuario
        # Esto debe cambiar al hacer la validación del usuario
        token = request.POST.get('token')
        print(token)
        # token = request.POST['token']

        uidUser = "uidUserTry"
        print(uidUser)
        # obtengo la información del auto a rentar
        # car = get_object_or_404(Car, id=request.POST.get('carId')) #cambiar por carId
        print("ahora a buscar auto")
        cars = Car.objects.filter(id=request.POST.get('carId'))
        car = cars[0]
        print("se encontró auto")
        print(car.id)
        # obtengo la información de la empresa rentadora del auto
        # rental = get_object_or_404(CarRental, id=request.POST.get('rentalId')) #cambiar por rentalId
        print("Ahora a buscar rental")
        # rentals = CarRental.objects.filter(id=request.POST.get('rentalId'))
        # rental = rentals[0]
        rental = car.rental
        print("se encontró rental")
        print(rental._id)

        # obtengo el resto de información
        # Fecha en la que se hizo la reserva
        bookingDate = request.POST.get('bookingDate')
        bookingDate = _parse_date(str(bookingDate))
        # pickup
        pickup = request.POST.get('pickup')
        # fecha en la que se recoge el auto -comienza la renta-
        pickupDate = request.POST.get('pickupDate')
        pickupDate = _parse_date(str(pickupDate))
        fromDate = pickupDate
        # Lugar donde se entregará el auto cuando finalice la renta
        deliverPlace = request.POST.get('deliverPlace')
        # fecha en la que se entrega el auto -fin de la renta-
        deliverDate = request.POST.get('deliverDate')
        deliverDate = _parse_date(str(deliverDate))
        toDate = deliverDate

        # se crea el objeto a guardar
        rent_saved = CarRent(
            car=car,
            token=token,
            uidUser=uidUser,
            bookingDate=bookingDate,
            pickup=pickup,
            pickupDate=pickupDate,
            deliverPlace=deliverPlace,
            deliverDate=deliverDate,
            rental=rental
        )
        rent_saved.save()

        # return
        return rent_saved
