from django.urls import path
from .views import current_weather_view

urlpatterns = [
    path('', current_weather_view),
]
