from rest_framework import serializers

from measurement.models import Measurement, Sensor


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'sensor', 'temperature', 'created_at']


class MeasurementSerializer(MeasurementFullSerializer):
    class Meta(MeasurementFullSerializer.Meta):
        fields = ['temperature', 'created_at']


class SensorDetailSerializer(SensorSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta(SensorSerializer.Meta):
        fields = SensorSerializer.Meta.fields + ['measurements']
