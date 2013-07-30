from django.db import models


class TemperatureReading(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    temperature = models.DecimalField(decimal_places=2,max_digits=5)
    sensor = models.IntegerField()
    date_time = models.DateTimeField()

    class Meta:
        ordering = ("created",)
