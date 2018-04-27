from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from cars.models import CarModel


class BuyModel(models.Model):
    boughtCar = models.CharField(max_length = 50000)

    def __str__(self):
        return self.boughtCar.__str__ + ' bought by ' + self.buyer.username