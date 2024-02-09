import requests
from weather.models import Weather


# todo
#  определние адреса для подстановки в запрос*
#  сокращение количества запросов:
#  делать запрос, когда информация о текущей погоде неактуальна


def weather_update_check():
    pass


def update_weather_data():
    data = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Saint Petersburg/today/?key=4BFH3CNBB54CB3J4QUMU99GSC')
    data = data.json()

    weather_data = Weather(
        location=data.get('address'),
        description=data.get('days')[0].get('description'),
        temperature=convert_fahrenheit_to_celsius(data.get('currentConditions').get('temp'))
    )
    weather_data.save()

    return weather_data


def convert_fahrenheit_to_celsius(temperature_fahrenheit):
    return round((temperature_fahrenheit - 32)/1.8)
