from django.db import models
from simple_history.models import HistoricalRecords


class DHTTemperature(models.Model):

    value = models.FloatField()
    timestamp = models.IntegerField()
    history = HistoricalRecords()


class DS18B20Temperature(models.Model):

    celcius_value = models.FloatField()
    farnheit_value = models.FloatField()
    timestamp = models.IntegerField()
    history = HistoricalRecords()


class Humidity(models.Model):

    value = models.FloatField()
    timestamp = models.IntegerField()
    history = HistoricalRecords()


class SoilMoisture(models.Model):

    water_detected = models.BooleanField()
    timestamp = models.IntegerField()
    history = HistoricalRecords()


class PeristaticPump(models.Model):

    running = models.BooleanField()
    timestamp = models.IntegerField()
    history = HistoricalRecords()


class Alert(models.Model):
	event = models.CharField(max_length=25)
	timestamp = models.IntegerField()
	history = HistoricalRecords()