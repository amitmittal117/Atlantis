from __future__ import unicode_literals

from django.db import models


# car_number, phone_number, license_number, email must be unique fields.

class BasicDetails(models.Model):
    email = models.CharField(primary_key=True)
    car_number = models.CharField(max_length=20, blank=False, unique=True)
    phone_number = models.CharField(max_length=20, blank=False, unique=True)
    license_number = models.CharField(max_length=20, blank=False, unique=True)
    name = models.CharField(max_length=20, blank=False)


class LocationOfCar(models.Model):
    license_number = models.CharField(primary_key=True)
    lat = models.CharField(max_length=10)
    lon = models.CharField(max_length=10)
