from django.shortcuts import render
from django.http import HttpResponse

def sensor_form(request):
    return render(request, 'nodemcu/sensor_form.html')

def sensor_data(request):
    if request.method == 'POST':
        sensor1_value = request.POST.get('sensor1')
        sensor2_value = request.POST.get('sensor2')
        
        print("Sensor 1 value:", sensor1_value)
        print("Sensor 2 value:", sensor2_value)
        
        # You can process the data further here
        
        return HttpResponse("Data received successfully.", status=200)
    else:
        return HttpResponse("Method not allowed.", status=405)
