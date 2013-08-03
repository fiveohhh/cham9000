# Create your views here.
from cham9000.api.models import TemperatureReading
from rest_framework import generics
from cham9000.api.serializers import TemperatureReadingSerializer
from django.utils.dateparse import parse_datetime

class TemperatureReadingList( generics.ListAPIView):
    queryset = TemperatureReading.objects.all()
    serializer_class = TemperatureReadingSerializer
    
    def get_queryset(self):
        queryset = TemperatureReading.objects.all()
        start_string =  self.request.QUERY_PARAMS.get('start_date',None )
        end_string = self.request.QUERY_PARAMS.get('end_date',None )
    
        # If both a valid startdate and end date were specified in the parameters
        if start_string != None and end_string != None:
            start_date = parse_datetime(start_string)
            end_date = parse_datetime(end_string)

            queryset = queryset.filter(date_time__range=(start_date,end_date))
        
        return queryset
        

class TemperatureReadingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TemperatureReading.objects.all()
    serializer_class = TemperatureReadingSerializer
