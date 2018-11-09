from django.db.models import CASCADE, IntegerField, CharField, ForeignKey, AutoField, Model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField


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
    rental = ForeignKey('Rental', on_delete=CASCADE)
    plate = IntegerField()
    rating = IntegerField(default=0, validators=[
                          MaxValueValidator(5), MinValueValidator(0)])
    capacity = IntegerField(default=1)
    transmission = CharField(max_length=20)
    doors = IntegerField(default=2)
    color = CharField(max_length=20)
    kms = IntegerField(default=0)
    pictures = ArrayField(CharField(max_length=2083), blank=True, size=20)
