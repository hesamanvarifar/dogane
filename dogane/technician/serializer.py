from rest_framework import serializers

from core.models import User, Car

class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['is_repaired']