from rest_framework import serializers
from core.models import Car

class ReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
        exclude = ['is_repaired', 'is_finished']

class UpdateReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["name"]