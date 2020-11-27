from carsapp.models import Car, CarRate
from carsapp.serializers import CarSerializer,CarRateSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CarViewSet(APIView):

    def get(self, request, format=None):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
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
