from django.shortcuts import render
from django.http import HttpResponse
from weather_api import current_weather_apiweather
from django.http import JsonResponse


# Create your views here.
def current_weather_view(request):
    if request.method == "GET":
        data = current_weather_apiweather("Saint-Petersburg")
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})
