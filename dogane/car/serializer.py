from rest_framework import serializers
from core.models import Car, CarPart

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPart
        fields = '__all__'