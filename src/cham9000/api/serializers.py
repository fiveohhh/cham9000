from rest_framework import serializers
from api.models import TemperatureReading

class TemperatureReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureReading
        fields = ('id', 'date_time', 'temperature', 'sensor')
