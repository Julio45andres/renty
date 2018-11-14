from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from .models import Rental, Car
from .serializers import RentalSerializer, CarSerializer, CarSerializerToSave, CarSearchSerializer


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
        _type = self.request.query_params.get('type', None)
        if _type is not None:
            queryset = queryset.filter(category__iexact=_type)

        _from = self.request.query_params.get('from', None)
        _from = 0 + int(_from)
        to = self.request.query_params.get('to', None)
        to = 0 + int(to)
        queryset = queryset[_from:to]
        # if model is not None:
        #     queryset = queryset.filter(model__iexact=model)
        return queryset