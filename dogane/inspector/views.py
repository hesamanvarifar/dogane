from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Car
from core.permission import IsInspector
from serializer import CarFinishedSerializer


class CarFinished(APIView):

    permission_classes = [IsInspector]

    def post(self, request, id):
        car = Car.objects.get(id=id)
        car.is_finished = True
        car.save()
        serializer = CarFinishedSerializer(car)

        return Response(serializer.data)