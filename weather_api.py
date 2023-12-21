import requests
from datetime import datetime

# Словарь перевода значений направления ветра
DIRECTION_TRANSFORM = {
    'N': 'северное',
    'NNE': 'северо-северо-восточное',
    'NE': 'северо-восточное',
    'ENE': 'восточно-северо-восточное',
    'E': 'восточное',
    'ESE': 'восточно-юго-восточное',
    'SE': 'юго-восточное',
    'SSE': 'юго-юго-восточное',
    'S': 'южное',
    'SSW': 'юго-юго-западное',
    'SW': 'юго-западное',
    'WSW': 'западно-юго-западное',
    'W': 'западное',
    'WNW': 'западно-северо-западное',
    'NW': 'северо-западное',
    'NNW': 'северо-северо-западное',
    'C': 'штиль',
}

def current_weather_apiweather(city) -> str:
    """Данная функция принимает 1 аргумент: название города на английском
    языке и возвращает:
    1) Название города
    2) Время обновления данных
    3) Дату
    4) Температуру, в градусах Цельсия
    5) Ощущаемую температуру, в градусах Цельсия
    6) Давление, в мм. ртутного столба
    7) Влажность, в %
    8) Скорость ветра, в м/с
    9) Порывы ветра, в м/с
    10) Направление ветра."""
    key = "6719b1354b964e308af85231232112"
    url = f"https://api.weatherapi.com/v1/current.json?key={key}&q={city}"
    response = requests.get(url)
    data = response.json()
    result = f"Город: {data['location']['name']}\n" \
             f"Время обновления данных: {datetime.fromisoformat(data['current']['last_updated']).time()}\n" \
             f"Дата: {datetime.fromtimestamp(data['current']['last_updated_epoch']).date().strftime('%d/%m/%Y')}\n" \
             f"Температура: {data['current']['temp_c']} C\n" \
             f"Ощущается как: {data['current']['feelslike_c']} C\n" \
             f"Давление: {data['current']['pressure_mb']*0.75:.1f} мм. ртутного столба\n" \
             f"Влажность: {data['current']['humidity']} %\n" \
             f"Скорость ветра: {data['current']['wind_kph']/3.6:.1f} м/с\n" \
             f"Порывы ветра: {data['current']['gust_kph']/3.6:.1f} м/с\n" \
             f"Направление ветра: {DIRECTION_TRANSFORM[data['current']['wind_dir']]}"
    return result

if __name__ == "__main__":
    city = input("Введите название города на английском языке: ")
    print(current_weather_apiweather(city))