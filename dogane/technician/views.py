from django.shortcuts import get_object_or_404, render

from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import  Car


class TechnicianView(APIView):
    def post(self,request,id):
        car:Car = get_object_or_404(Car, id=id)
        car.is_repaired = True
        car.save()
        return Response(status=200)
