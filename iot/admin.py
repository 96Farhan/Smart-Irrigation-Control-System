
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import DHTTemperature, DS18B20Temperature, Humidity
from .models import SoilMoisture, PeristaticPump, Alert


admin.site.register(DHTTemperature, SimpleHistoryAdmin)
admin.site.register(Humidity, SimpleHistoryAdmin)
admin.site.register(DS18B20Temperature, SimpleHistoryAdmin)
admin.site.register(SoilMoisture, SimpleHistoryAdmin)
admin.site.register(PeristaticPump, SimpleHistoryAdmin)
admin.site.register(Alert, SimpleHistoryAdmin)


