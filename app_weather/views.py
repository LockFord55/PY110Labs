from django.shortcuts import render
from django.http import HttpResponse
from weather_api import current_weather_apiweather
from django.http import JsonResponse


# Create your views here.
def current_weather_view(request):
    if request.method == "GET":
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')
        if lat and lon:
            data = current_weather_apiweather(lat=lat, lon=lon)
        else:
            data = current_weather_apiweather(59.93, 30.31)
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})
