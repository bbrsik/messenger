import requests
from django.http import JsonResponse


# todo
#  определние адреса для подстановки в запрос*
#  сокращение количества запросов:
#  делать запрос, когда информация о текущей погоде неактуальна

def get_weather_data():
    data = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Saint Petersburg/today/?key=4BFH3CNBB54CB3J4QUMU99GSC')
    data = data.json()

    weather_data = {
        'location': data.get('address'),
        'description': data.get('days')[0].get('description'),
        'temp': convert_fahrenheit_to_celsius(data.get('currentConditions').get('temp')),
        }

    return weather_data


def convert_fahrenheit_to_celsius(temperature_fahrenheit):
    return round((temperature_fahrenheit - 32)/1.8)
