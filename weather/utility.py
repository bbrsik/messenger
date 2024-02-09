import requests
import datetime
from weather.models import Weather
from django.http import JsonResponse


# todo
#  определние адреса для подстановки в запрос*
#  сокращение количества запросов:
#  делать запрос, когда информация о текущей погоде неактуальна


def weather_update_check():
    last_update = Weather.objects.latest("created_at").created_at
    print(last_update)
    current_time = datetime.datetime.now()
    current_time = current_time.replace(tzinfo=None)
    print(current_time)
    difference = current_time - last_update
    print(difference)
    return


def update_weather_data():
    location = 'Saint Petersburg'
    key = '4BFH3CNBB54CB3J4QUMU99GSC'
    url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{0}/today/?key={1}'.format(location, key)

    data = requests.get(url)
    print(data)
    data = data.json()
    print(data)
    if 0 == 1:
        print("returning fail response")
        return JsonResponse({}, status=502)

    weather_data = Weather(
        location=data.get('address'),
        description=data.get('days')[0].get('description'),
        temperature=convert_fahrenheit_to_celsius(data.get('currentConditions').get('temp'))
    )
    weather_data.save()

    print(weather_data)
    return JsonResponse({}, status=200)


def convert_fahrenheit_to_celsius(temperature_fahrenheit):
    return round((temperature_fahrenheit - 32)/1.8)
