from .models import Doctor,Availability
from rest_framework import serializers


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'


class AvailableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Availability

        fields = '__all__'
