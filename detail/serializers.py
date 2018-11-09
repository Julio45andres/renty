from rest_framework import serializers
from .models import Rental, Car


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ('id', 'name')


class PictureSerializer(serializers.Serializer):
    url = serializers.CharField(source='celery_state', max_length=2083)

    def __init__(self, *args, **kwargs):
        super(PictureSerializer, self).__init__(*args, **kwargs)
        if kwargs.get('many', False):
            self.fields.pop('celery_state')


class CarSerializer(serializers.ModelSerializer):
    pictures = serializers.StringRelatedField(many=True)

    class Meta:
        model = Car
        fields = ('id', 'brand', 'thumbnail', 'price', 'category',
                  'model', 'rental', 'plate', 'rating', 'capacity', 'transmission',
                  'doors', 'color', 'kms', 'pictures'
                  )
