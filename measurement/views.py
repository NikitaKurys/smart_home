from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
import json

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer


class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        new_sensor = Sensor(title=request.data['title'],
                            description=request.data['description'])
        new_sensor.save()
        return Response({'status': 'ОК'})


class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        # new_team = Team(
        #     nickname=team_name,
        #     employee_id=employee_id,
        #     department_id=Department.objects.get(password=password, department_name=department_name)
        # )
        sens = Sensor.objects.all()
        print(sens[request.data['sensor']])
        new_measurement = Measurement(temperature=request.data['temperature'], sensorID=sens[request.data['sensor']])
        new_measurement.save()
        return Response({'status': 'ОК'})


class SensorList(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def patch(self, request, pk):
        id = int(pk) - 1
        sens = Sensor.objects.all()
        changes_sensor = Sensor(id=sens[id].id,
                                title=sens[id].title,
                                description=request.data['description'])
        changes_sensor.save()
        return Response({'status': 'OK'})



