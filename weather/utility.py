import requests
import datetime
import os
from weather.models import Weather
from django.utils import timezone


def weather_update_check(location='Saint Petersburg'):
    if Weather.objects.count() != 0:
        last_update = Weather.objects.latest("created_at").created_at
        current_time = timezone.now()
        difference = current_time - last_update
        max_difference = datetime.timedelta(hours=1)
        if difference < max_difference:
            return False

    weather_data = update_weather_data(location)
    return weather_data


def update_weather_data(location='Saint Petersburg'):
    # todo список городов на выбор пользователя
    key = os.getenv("WEATHER_API_KEY")
    url = ('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{0}/today/?key={1}'
           .format(location, key))

    response = requests.get(url)
    data = response.json()

    weather_data = {
        'location': data.get('address'),
        'description': data.get('days')[0].get('description'),
        'temperature': convert_fahrenheit_to_celsius(data.get('currentConditions').get('temp'))
    }

    return weather_data


def convert_fahrenheit_to_celsius(temperature_fahrenheit):
    return round((temperature_fahrenheit - 32)/1.8)
