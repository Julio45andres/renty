from rest_framework import serializers
from .models import CarRental, Car, CarRent
from rest_framework.fields import ListField


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarRental
        fields = ('id', 'name')


RentalSerializer._declared_fields["id"] = serializers.IntegerField(
    source="_id")


class PictureSerializer(serializers.Serializer):
    url = serializers.CharField(source='celery_state', max_length=2083)

    def __init__(self, *args, **kwargs):
        super(PictureSerializer, self).__init__(*args, **kwargs)
        if kwargs.get('many', False):
            self.fields.pop('celery_state')


class CarSerializer(serializers.ModelSerializer):
    pictures = serializers.ListField(
        child=serializers.CharField(max_length=2083))
    rental = RentalSerializer(read_only=True)

    class Meta:
        model = Car
        fields = ('id', 'brand', 'thumbnail', 'price', 'type',
                  'model', 'rental', 'plate', 'rating', 'capacity', 'transmission',
                  'doors', 'color', 'kms', 'pictures'
                  )


CarSerializer._declared_fields["type"] = serializers.CharField(
    source="category")


class CarSerializerToSave(serializers.ModelSerializer):
    pictures = serializers.ListField(
        child=serializers.CharField(max_length=2083))

    class Meta:
        model = Car
        fields = ('id', 'brand', 'thumbnail', 'price', 'type',
                  'model', 'rental', 'plate', 'rating', 'capacity', 'transmission',
                  'doors', 'color', 'kms', 'pictures'
                  )


CarSerializerToSave._declared_fields["type"] = serializers.CharField(
    source="category")


class CarSearchSerializer(serializers.HyperlinkedModelSerializer):
    rental = RentalSerializer(read_only=True)

    class Meta:
        model = Car
        fields = ('id', 'brand', 'thumbnail', 'price', 'type',
                  'model', 'rental'
                  )


CarSearchSerializer._declared_fields["type"] = serializers.CharField(
    source="category")


class StringListField(serializers.ListField):
    child = serializers.CharField()


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarRent
        fields = (
            'bookingId',
            'token',
            'car',
            'bookingDate',
            'pickup',
            'pickupDate',
            'deliverPlace',
            'deliverDate',
            'rental'
        )


ReservationSerializer._declared_fields["bookingId"] = serializers.IntegerField(
    source="id")
