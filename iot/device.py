from iot.models import DHTTemperature, DS18B20Temperature, Humidity
from iot.models import SoilMoisture, PeristaticPump, Alert
import time


def update_dht_temp(dht_temp_value):
	dht_temp = DHTTemperature.objects.all()
	for temp in dht_temp:
	    temp.value = dht_temp_value
	    temp.timestamp = int(time.time())
	    temp.save()


def update_ds_temp(ds18b20_celcius_value, ds18b20_farenheit_value):
    ds_temp = DS18B20Temperature.objects.all()
    for temp in ds_temp:
        temp.celcius_value = ds18b20_celcius_value
        temp.farnheit_value = ds18b20_farenheit_value
        temp.timestamp = int(time.time())
        temp.save()


def update_humidity(value):
    humidity = Humidity.objects.all()
    for instance in humidity:
        instance.value = value
        instance.timestamp = int(time.time())
        instance.save()


def soil_moisture_status(soil_moisture_output):
    soil_moisture = SoilMoisture.objects.all()
    for instance in soil_moisture:
        if soil_moisture_output == 'Yes' and instance.water_detected != True:
            instance.water_detected = True
            alert = Alert(event="Water Detected", timestamp=int(time.time()))
            alert.save()
        elif soil_moisture_output == 'No' and instance.water_detected == True:
            instance.water_detected = False
        instance.timestamp = int(time.time())
        instance.save()


def pump_status(peristatic_pump):
    pump = PeristaticPump.objects.all()
    for instance in pump:
        if peristatic_pump == 'Yes' and instance.running != True:
            instance.running = True
            alert = Alert(event="Pump Running", timestamp=int(time.time()))
            alert.save()
        elif peristatic_pump == 'No' and instance.running == True:
            instance.running = False
        instance.timestamp = int(time.time())
        instance.save()