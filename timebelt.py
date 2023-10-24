import asyncio
import time
from aiohttp import ClientSession


async def get_weather(city):
    async with ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': 'fdaa73c78f46312cae2d1570af1880d9'}

        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            print(f'{city}: {weather_json["weather"][0]["main"]}')


async def main(cities_):
    tasks = []
    for city in cities_:
        tasks.append(asyncio.create_task(get_weather(city)))

    for task in tasks:
        await task


cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
          'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']

print(time.strftime('%X'))

asyncio.run(main(cities))

print(time.strftime('%X'))