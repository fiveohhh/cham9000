from django.conf.urls.defaults import patterns, url

from api.views import TemperatureReadingList, TemperatureReadingDetail


urlpatterns = patterns('api.views',

    url(r'temperatures/$', TemperatureReadingList.as_view(),name='temperatureReading-list'),
    url(r'temperatures/(?P<pk>[0-9]+)/$', TemperatureReadingDetail.as_view(), name='temperatureReading-detail'),
)
