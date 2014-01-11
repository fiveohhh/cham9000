from rest_framework import serializers
from cham9000.api.models import TemperatureReading

class TemperatureReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureReading
        fields = ('id', 'date_time', 'temperature', 'sensor')
