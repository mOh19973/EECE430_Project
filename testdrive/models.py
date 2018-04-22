from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from cars.models import CarModel
from datetime import datetime


class TDModel(models.Model):
    driveDate = models.DateTimeField('Test Drive Date', default=datetime.now)
    driveCar = models.ForeignKey(CarModel, on_delete=models.CASCADE, default=1)
    driver = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def get_absolute_url(self):
        return reverse('testdrive:detail:', kwargs={'driveDate': self.driveDate})

    def __str__(self):
        return self.driveDate.__str__() + ' for ' + self.driveCar.__str__() \
               + ' scheduled for ' + self.driver.username