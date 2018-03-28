from django.db import models
from django.core.urlresolvers import reverse

class CarModel(models.Model):
    CarImg = models.FileField()
    CarBrand = models.CharField(max_length=45)
    Model = models.CharField(max_length=45)
    Year = models.CharField(max_length=40)
    Engine = models.CharField(max_length=40)
    Cylinders = models.CharField(max_length=16)
    DoorsNum = models.CharField(max_length=40)
    Weight = models.CharField(max_length=40)
    Fuel = models.CharField(max_length=15)
    BodyType = models.CharField(max_length=20)
    Transmission = models.CharField(max_length=45)
    HP = models.CharField(max_length=40)
    TopSpeed = models.CharField(max_length=40)
    FuelCapacity = models.CharField(max_length=40)
    Country = models.CharField(max_length=45)
    Mileage = models.CharField(max_length=40)
    Color = models.CharField(max_length=45)

    def get_absolute_url(self):
        return reverse('cars:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.CarBrand + ' - ' + self.Model + ' ' + self.Year
