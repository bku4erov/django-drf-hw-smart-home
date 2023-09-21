from models import Measurement, Sensor
from rest_framework import serializers


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'sensor', 'temperature', 'created_at']


class SensorDetailSerializer(SensorSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)
