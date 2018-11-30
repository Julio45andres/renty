from django.db.models import CASCADE, IntegerField, CharField, DateField, ForeignKey, AutoField, Model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField
from datetime import datetime


class CarRental(Model):
    id = AutoField(primary_key=True)
    _id = IntegerField(default=967543461)
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
    rental = ForeignKey('CarRental', on_delete=CASCADE)
    plate = IntegerField()
    rating = IntegerField(default=0, validators=[
        MaxValueValidator(5), MinValueValidator(0)])
    capacity = IntegerField(default=1)
    transmission = CharField(default="Mecanica", max_length=20)
    doors = IntegerField(default=1, validators=[
        MinValueValidator(1), MaxValueValidator(7)])
    color = CharField(max_length=20)
    kms = IntegerField(default=0)
    pictures = ArrayField(CharField(max_length=2083), blank=True, size=20)


class CarRent(Model):
    id = AutoField(primary_key=True)
    car = ForeignKey('Car', on_delete=CASCADE)
    token = CharField(default="defaultToke", max_length=2000)
    uidUser = CharField(default="defaultUidUser", max_length=2000)
    bookingDate = DateField()
    pickup = CharField(default="Aeropuerto", max_length=100)
    pickupDate = DateField()
    deliverPlace = CharField(default="Aeropuerto", max_length=100)
    deliverDate = DateField()
    rental = ForeignKey('CarRental', on_delete=CASCADE, default=1)
