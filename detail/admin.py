from django.contrib import admin
from .models import Car, Rental, Reservation

# Register your models here.
admin.site.register(Car)
admin.site.register(Rental)
admin.site.register(Reservation)
