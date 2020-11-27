from .models import Car, CarRate
from rest_framework import serializers


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['id','car_name', 'car_make']

class CarRateSerializer(serializers.HyperlinkedModelSerializer):
    related_car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())
    class Meta:
        model = CarRate
        fields = ['id','rate_value', 'rate_car_foreignkey']
