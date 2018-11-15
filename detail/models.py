from django.db.models import CASCADE, IntegerField, CharField, DateField, ForeignKey, AutoField, Model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField
from datetime import datetime


class Rental(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)


class Car(Model):
    id = AutoField(primary_key=True)
    brand = CharField(max_length=50)
    # Tamaño url: https://bit.ly/2JNxbmP
    thumbnail = CharField(max_length=2083)
    price = IntegerField()
    # type y class son palabras reservadas
    category = CharField(max_length=50)
    model = CharField(max_length=50)
    pickup = CharField(default="Aeropuerto", max_length=100)
    rental = ForeignKey('Rental', on_delete=CASCADE)
    plate = IntegerField()
    rating = IntegerField(default=0, validators=[
                          MaxValueValidator(5), MinValueValidator(0)])
    capacity = IntegerField(default=1)
    transmission = CharField(default="Mecanica", max_length=20)
    doors = IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(7)])
    color = CharField(max_length=20)
    kms = IntegerField(default=0)
    pictures = ArrayField(CharField(max_length=2083), blank=True, size=20)

class Reservation(Model):
    id = AutoField(primary_key=True)
    car = ForeignKey('Car', on_delete=CASCADE)
    fromDate = DateField()
    toDate = DateField()
