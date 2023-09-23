from rest_framework import generics

from measurement.models import Measurement, Sensor
from measurement.serializers import (MeasurementFullSerializer,
                                     SensorDetailSerializer, SensorSerializer)


class SensorList(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorDetail(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasurementView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementFullSerializer