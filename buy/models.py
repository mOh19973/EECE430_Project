from django.contrib.auth.models import User
from django.db import models


class BuyModel(models.Model):
    boughtCar = models.CharField(max_length = 50000)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.boughtCar.__str__ + ' bought by ' + self.buyer.username
