import datetime
from asgiref.sync import async_to_sync
from channels.consumer import SyncConsumer
from iot.device import update_dht_temp, update_ds_temp, update_humidity
from iot.device import soil_moisture_status, pump_status


class MqttConsumer(SyncConsumer):

    def mqtt_sub(self, event):
        topic = event['text']['topic']
        payload = event['text']
        data = payload['payload']
        dht_temp_value = data['DHT_Temp_Value']
        humidity_value = data['Humidity_Value']
        ds18b20_celcius_value = data['DS18B20_Celcius_Value']
        ds18b20_farenheit_value = data['DS18B20_Farenheit_Value']
        soil_moisture_output = data['Soil_Moisture_Output']
        peristatic_pump = data['Peristatic_Pump']
        print(data)
        update_dht_temp(dht_temp_value)
        update_humidity(humidity_value)
        update_ds_temp(ds18b20_celcius_value, ds18b20_farenheit_value)
        soil_moisture_status(soil_moisture_output)
        pump_status(peristatic_pump)
        