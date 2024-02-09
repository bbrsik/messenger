import requests
import datetime
import os
from weather.models import Weather
from django.http import JsonResponse
from dotenv import load_dotenv
from django.core.exceptions import ObjectDoesNotExist


def weather_update_check():
    try:
        last_update = Weather.objects.latest("created_at").created_at.replace(tzinfo=None)
    except ObjectDoesNotExist:
        print("CREATING WEATHER REPORT")
        update_weather_data()
        return JsonResponse({}, status=200)

    current_time = datetime.datetime.utcnow()
    difference = current_time - last_update
    max_difference = datetime.timedelta(hours=1)

    if difference >= max_difference:
        print("UPDATING WEATHER REPORT")
        update_weather_data()
        return JsonResponse({}, status=200)
    return JsonResponse({}, status=200)


def update_weather_data():
    load_dotenv()
    location = 'Saint Petersburg' #todo список городов на выбор пользователя
    key = os.getenv("WEATHER_API_KEY")
    url = ('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{0}/today/?key={1}'
           .format(location, key))

    data = requests.get(url)
    data = data.json()

    weather_data = Weather(
        location=data.get('address'),
        description=data.get('days')[0].get('description'),
        temperature=convert_fahrenheit_to_celsius(data.get('currentConditions').get('temp'))
    )
    weather_data.save()
    return JsonResponse({}, status=200)


def convert_fahrenheit_to_celsius(temperature_fahrenheit):
    return round((temperature_fahrenheit - 32)/1.8)
