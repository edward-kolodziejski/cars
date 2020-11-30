from django.db import models


class Car(models.Model):
    car_make = models.CharField(max_length=50)
    car_name = models.CharField(max_length=50)

class CarRate(models.Model):
    rate_value = models.IntegerField()
    rate_car_foreignkey = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='rates')