# Create your views here.
from cham9000.api.models import TemperatureReading
from rest_framework import generics,filters
import django_filters
from cham9000.api.serializers import TemperatureReadingSerializer
from django.utils.dateparse import parse_datetime



class TemperatureReadingFilter(django_filters.FilterSet):
    min_temp = django_filters.NumberFilter(lookup_type='gte', name='temperature')
    max_temp = django_filters.NumberFilter(lookup_type='lte', name='temperature')
    
    class Meta:
        model = TemperatureReading
        fields = ['sensor','date_time','min_temp','max_temp']


class TemperatureReadingList( generics.ListAPIView):
    queryset = TemperatureReading.objects.all()
    serializer_class = TemperatureReadingSerializer

    paginate_by = 150
    paginate_by_param = 'page_size'
    
    filter_class = TemperatureReadingFilter
    ordering = ('-date_time',)
    def get_queryset(self):
        queryset = TemperatureReading.objects.all()
        start_string =  str(self.request.QUERY_PARAMS.get('start_date',None ))
        end_string = str(self.request.QUERY_PARAMS.get('end_date',None ))

        start_date = parse_datetime(start_string)
        end_date = parse_datetime(end_string)
        
        if end_date != None:
            queryset = queryset.filter(date_time__lte=end_date)
        if start_date != None:
            queryset = queryset.filter(date_time__gte=start_date)

        return queryset.order_by('-date_time')

class TemperatureReadingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TemperatureReading.objects.all()
    serializer_class = TemperatureReadingSerializer
