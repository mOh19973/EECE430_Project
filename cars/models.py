from django.db import models


class CarModel(models.Model):
    CarImg = models.CharField(max_length=50000)
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

    def __str__(self):
        return self.CarBrand + ' - ' + self.Model + ' ' + self.Year

    class Meta:
        verbose_name_plural = "Car Models"

#class Administrator(models.Model):
#    username = models.CharField(max_length=255)
#    password = models.CharField(max_length=255)
#    full_name= models.CharField(max_length=255)

#    def __str__(self):
#        return self.full_name


class Customer(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    full_name= models.CharField(max_length=255)

    # ADD ALL THE OTHER ATTRIBUTES


    def __str__(self):
        return self.full_name
