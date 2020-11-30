from django.db import models
from .models import Car, CarRate
from rest_framework import serializers


class CarRateSerializer(serializers.HyperlinkedModelSerializer):
    rate_car_foreignkey = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())
    class Meta:
        model = CarRate
        fields = ['id','rate_value', 'rate_car_foreignkey']

class CarSerializer(serializers.HyperlinkedModelSerializer):
    rates = CarRateSerializer(read_only=True, many=True)
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Car
        fields = ['id','car_name', 'car_make','rates', 'rating']

    def get_rating(self, obj):
        print(obj.rates.all())
        print(obj.rates.all().aggregate(models.Avg('rate_value')))
        average = obj.rates.all().aggregate(models.Avg('rate_value'))['rate_value__avg']
        if average == None:
            return 0
        return average