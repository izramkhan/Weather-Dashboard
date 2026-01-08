import requests
from datetime import datetime

def get_weather(city):

    api_key = '2b7bc619685af934d31083818594d669'

    weather_link = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}'
        )

    weather_data = weather_link.json()

    if weather_data.get('cod') != 200:
        return None
    
    city = weather_data['name']
    weather = weather_data['weather'][0]['main']
    temp = weather_data['main']['temp']
    temp_min = weather_data['main']['temp_min']
    temp_max = weather_data['main']['temp_max']
    wind_speed = weather_data['wind']['speed']
    wind_temp = weather_data['wind']['deg']
    pressure = weather_data['main']['pressure']
    humidity = weather_data['main']['humidity']
    condition = weather_data['weather'][0]['description']
    country = weather_data['sys']['country']

    # Getting the local time of the city
    local_timestamp = weather_data['dt'] + weather_data['timezone']
    local_timestamp = datetime.utcfromtimestamp(local_timestamp)

    local_time = local_timestamp.strftime('%A, %I:%M %p')


    weather_dict = {
        'country':country,
        'city': city,
        'weather': weather,
        'temperature': temp,
        'max temperature': temp_max,
        'min temperature': temp_min,
        'wind speed': wind_speed,
        'wind temp': wind_temp,
        'pressure': pressure,
        'humidity': humidity,
        'condition': condition,
        'local time': local_time

    }

    return weather_dict
