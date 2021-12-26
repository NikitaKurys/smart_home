from django.contrib import admin
from django.urls import path

from measurement.views import SensorView, MeasurementView, SensorList

urlpatterns = [
    path('sensor/', SensorView.as_view()),
    path('measurement/', MeasurementView.as_view()),
    path('sensor/<pk>/', SensorList.as_view())
]
