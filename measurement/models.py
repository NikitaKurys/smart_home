from django.db import models


class Sensor(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=50)


class Measurement(models.Model):
    sensorID = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='Sens_id')
    temperature = models.IntegerField()
    date = models.DateField(auto_now_add=True)


