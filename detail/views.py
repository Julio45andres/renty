from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from .models import Rental, Car
from .serializers import RentalSerializer, CarSerializer, CarSerializerToSave, CarSearchSerializer
from django.http import Http404

class RentalView(generics.ListAPIView):
    serializer_class = RentalSerializer

    def get_queryset(self):
        queryset = Rental.objects.all()
        return queryset

    def post(self, request):
        serializer = RentalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarView(generics.ListAPIView):
    serializer_class = CarSerializer
    lookup_url_kwarg="carid"

    def get_queryset(self):
        carid = self.kwargs.get(self.lookup_url_kwarg)
        queryset = Car.objects.all()
        if carid is not None:
            queryset = queryset.filter(id=carid)
        return queryset

    def post(self, request):
        serializer = CarSerializerToSave(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarSearchView(generics.ListAPIView):
    serializer_class = CarSearchSerializer

    def get_queryset(self):
        queryset = Car.objects.all()
        # type es una palabra reservada de python
        _type = self.request.query_params.get('type', None)
        pickup = self.request.query_params.get('pickup', None)
        if _type is not None:
            queryset = queryset.filter(category__iexact=_type)
        if pickup is not None:
            queryset = queryset.filter(pickup__iexact=pickup)
        _from = self.request.query_params.get('from', '0')
        _from = int(_from)
        to = self.request.query_params.get('to', '0')
        to = int(to)
        queryset = queryset[_from:to]
        return queryset