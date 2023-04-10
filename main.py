#virtualenv venv
#source version/bin/activate.fish
#pip install requests
#pip install python-dotenv
#pip freeze> requerements.txt
#Perekluchit interpritator

import requests
from dotenv import load_dotenv
from os import getenv
load_dotenv()

#8a27d483ee8c053eb537a4b7388dcb72
# p = getenv('passw')
# a = getenv('login')
# b = getenv('email')
# print(p, a, b)

# weatheApi =getenv('WeatherApi')
# # city = input('Vvvedite nazvanie goroda: ')
# city = "Almaty"
# url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weatheApi}&units=metric'

# response = requests.get(url)
# data = response.json()
# print(data)

# d5bb44d0fa8e39e2339c9019d833d826
import requests
from datetime import datetime
# from pprint import pprint
from os import getenv, system
from dotenv import load_dotenv
load_dotenv()

WEATHER_API = getenv('WEATHER_API')
# city = input("Введите газвание города: ")


def weather_service(get_city,API=WEATHER_API):
    """Ваш бот-метеоролог мгновенно показывает погоду в любом городе,
    предоставляя актуальную информацию о температуре воздуха, влажности и вероятности дождя. 
    Это помогает планировать дела эффективнее и быть в курсе погодных событий 
    в режиме реального времени.

    get_city = 'Almaty'
    API = Weather_API

    weather_service(get_city :str, API=WEATHER_API) -> str:

    """

    url = f'https://api.openweathermap.org/data/2.5/weather?q={get_city}&appid={API}&units=metric'

    response = requests.get(url)
    data = response.json()

    # pprint(data)
    print(len(data))

    Pr_day = datetime.fromtimestamp(data['sys']['sunset']) - datetime.fromtimestamp(data['sys']['sunrise'])
    information = f"""Pogoda Daniyar
    Strana: {data['sys']['country']}
    Nazvanie goroda: {data['name']} {data['weather'][0]['description']} {data['clouds']['all']}%
    Temperature : {data['main']['temp']}°C
    Oshushaetsya : {data['main']['feels_like']}°C
    vlazhnost : {data['main']['humidity']}%
    davlenie vozduha : {data['main']['pressure']} gPa
    skorost vetra : {data['wind']['speed']}m/s
    Napravlenie : {data['wind']['deg']}°
    Voshod solnca : {datetime.fromtimestamp(data['sys']['sunrise'])}
    Prodolzhitelnost dnya : {Pr_day}
    Zakat solnca : {datetime.fromtimestamp(data['sys']['sunset'])}
    """

    return(information)
print(weather_service("Almaty"))