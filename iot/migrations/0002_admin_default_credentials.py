# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations
from django.contrib.auth.models import User
import time


def create_database(apps, schema_editor):
    if not (User.objects.filter(username='iot-admin').exists()):
        User.objects.create_superuser(
            username='iot-admin',
            password='iot-admin',
            email='admin@gmail.com'
        )

    dht_temp = apps.get_model("iot", "DHTTemperature")
    humidity = apps.get_model("iot", "Humidity")
    ds_temp = apps.get_model("iot", "DS18B20Temperature")
    soil_moisture = apps.get_model("iot", "SoilMoisture")
    pump = apps.get_model("iot", "PeristaticPump")

    dht_temp.objects.create(
        value=0,
        timestamp=int(time.time())
    )
    humidity.objects.create(
        value=0,
        timestamp=int(time.time())
    )
    ds_temp.objects.create(
        celcius_value=0,
        farnheit_value = 0,
        timestamp=int(time.time())
    )
    soil_moisture.objects.create(
        water_detected=False,
        timestamp=int(time.time())
    )
    pump.objects.create(
        running=False,
        timestamp=int(time.time())
    )


class Migration(migrations.Migration):

    dependencies = [('iot', '0001_initial'), ]
    operations = [migrations.RunPython(create_database)]
