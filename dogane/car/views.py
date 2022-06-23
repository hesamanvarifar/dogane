from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework import authentication, permissions
from core. models import Car,CarPart
from .serializer import CarSerializer,PartSerializer


class CarList(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

class CarDetail(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer = CarSerializer(queryset, many=True)     
    permission_classes = [permissions.IsAuthenticated]


class PartList(APIView):
    def get(self, request):
        parts = CarPart.objects.all()
        serializer = PartSerializer(parts, many=True)
        return Response(serializer.data)


