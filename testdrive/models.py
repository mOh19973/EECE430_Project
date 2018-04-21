from django.contrib.auth.models import User
from django.db import models
from cars.models import CarModel
from datetime import datetime


class TDModel(models.Model):
    driveDate = models.DateTimeField('Test Drive Date', default=datetime.now)
    driveCar = models.ForeignKey(CarModel, on_delete=models.CASCADE, default=1)
    driver = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
