from django.contrib import admin
from .models import Sensor, Measurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    pass


@admin.register(Measurement)
class SensorAdmin(admin.ModelAdmin):
    pass
# Register your models here.
