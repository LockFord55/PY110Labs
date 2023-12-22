from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def datetime_view(request):
    if request.method == "GET":
        data = f"Текущая дата и время: {datetime.now()}\n"
        return HttpResponse(data)