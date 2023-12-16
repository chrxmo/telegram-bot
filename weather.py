import requests
from pprint import pprint
from config import open_weather_token

lat = 56.843416
lon = 60.647221

def weather(lat, lon, open_weather_token):

    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        tempr = data['main']['temp']
        max_tempr = data['main']['temp_max']
        min_tempr = data['main']['temp_min']
        wind = data['wind']['speed']


        return f'В Екатеринубрге сегодня {tempr} градуса(-ов), максимальная температура: {max_tempr}, минимальная: {min_tempr}, скорость ветра {wind} м/c'
    except Exception as ex:
        print(ex)
