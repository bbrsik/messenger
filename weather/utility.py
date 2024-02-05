import requests
from django.http import JsonResponse


# todo
#  определние адреса для подстановки в вопрос
#  сокращение количества запросов:
#  запрос во время запуска сервера, запрос в 00:00

def get_weather_data(request):
    if request.method != "GET":
        return JsonResponse({}, status=400)
    data = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Saint Petersburg/today/?key=4BFH3CNBB54CB3J4QUMU99GSC')
    data = data.json()

    weather_data = \
        {
        'location': data.get('address'),
        'description': data.get('days')[0].get('description'),
        'temp': round((data.get('currentConditions').get('temp') - 32) / 1.8),
        }

    return weather_data
