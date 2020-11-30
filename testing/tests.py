import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from carsapp.models import Car, CarRate
from carsapp.serializers import CarSerializer, CarRateSerializer


# initialize the APIClient app
client = Client()