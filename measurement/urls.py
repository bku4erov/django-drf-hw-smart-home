from django.urls import path

from measurement.views import MeasurementView, SensorDetail, SensorList

urlpatterns = [
    path('sensors/', SensorList.as_view(), name='sensors'),
    path('sensors/<pk>/', SensorDetail.as_view(), name='sensors_detail'),
    path('measurements/', MeasurementView.as_view(), name='sensors_detail')
]
