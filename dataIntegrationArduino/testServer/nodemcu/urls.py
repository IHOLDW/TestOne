from django.urls import path
from nodemcu.views import sensor_form, sensor_data

urlpatterns = [
    path('sensor_form/', sensor_form, name='sensor_form'),
    path('sensor_data/', sensor_data, name='sensor_data'),
]
