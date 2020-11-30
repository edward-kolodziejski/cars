import requests
from .models import Car, CarRate
from .serializers import CarSerializer,CarRateSerializer
from django.db import models
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json


class CarViewSet(APIView):

    def get(self, request, format=None):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        make= body['car_make']
        name = body['car_name'].lower()
        serializer = CarSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        request_url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/'
        try:
            all_models_for_make = requests.get(f'{request_url}{make}', params='format=json')
            all_models_for_make_parsed = json.loads(all_models_for_make.text) #json parser/library from text to object 
            is_in_maked = False
            for result in all_models_for_make_parsed['Results']:
                if result['Model_Name'].lower() == name: # check if this model is in
                    is_in_maked = True
            if is_in_maked:
                serializer.save() # if exists  then save
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response('There is no cars of this manufactorer') #if not exists send error doesnt exist
        except:
            return Response('We could not verify if car belong to this manufuctorer') #if not exists send error doesnt exist

class CarRateViewSet(APIView):

    def get(self, request, format=None):
        rates = CarRate.objects.all()
        serializer = CarRateSerializer(rates, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarRateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PopularCarViewSet(APIView):

    def get(self, request, format=None):
        top = Car.objects.all().annotate(rating=models.Avg('rates__rate_value')).order_by('-rating')
        serializer = CarSerializer(top, many=True, context={'request': request})
        return Response(serializer.data)
