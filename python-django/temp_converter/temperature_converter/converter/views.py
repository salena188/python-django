from django.core.serializers import python
from django.db.models.expressions import result
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'form.html')

def convert_temperature(request):
    result = None
    unit = None
    if request.method == 'POST':
        temperature = request.POST['temperature']
        scale = request.POST['scale']
        if temperature :
            print(temperature)
            print(scale)
            temperature = float(temperature)
            if scale == 'Celsius':
                result = temperature * 9 / 5 + 32
                unit = 'Fahrenheit'
            elif scale == 'Fahrenheit':
                result = temperature - 32 *5 / 9
                unit = 'Celsius'
            print(result)
            print(unit)
    return render(request, 'result.html',{'result':result, 'unit':unit})