
from django.shortcuts import render
from core import permission
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


from .serializer import ReceptionSerializer,UpdateReceptionSerializer

class  Reception(APIView):

    permission_classes = [permission.IsReception]

    def post(self, request):
        serializer = ReceptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    # def patch(self, request, pk):
    #     serializer = ReceptionSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UpdateReception(APIView):
    permission_classes = [permission.IsReception]

    def patch(self, request, pk):
        serializer = UpdateReceptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    