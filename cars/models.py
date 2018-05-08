from django.db import models
from django.urls import reverse
from datetime import datetime


class CarModel(models.Model):
    CarImg = models.ImageField(upload_to='media', default='media/default.jpg')
    CarBrand = models.CharField(max_length=5000)
    Model = models.CharField(max_length=5000)
    Year = models.DateField('Year of Manufacture', default=datetime.now)
    Engine = models.FloatField(default=1.0)
    Cylinders = models.CharField(max_length=5000)
    DoorsNum = models.IntegerField(default=4)
    Weight = models.IntegerField(default=1000)
    Fuel = models.CharField(max_length=5000)
    BodyType = models.CharField(max_length=5000)
    Transmission = models.CharField(max_length=5000)
    HP = models.IntegerField(default=100)
    TopSpeed = models.IntegerField(default=220)
    FuelCapacity = models.IntegerField(default=50)
    Country = models.CharField(max_length=5000)
    Mileage = models.IntegerField(default=0)
    Color = models.CharField(max_length=5000)

    def get_absolute_url(self):
        return reverse('cars:detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.CarBrand + ' - ' + self.Model + ' ' + str(self.Year.year)
