
import requests


class WeatherAPI:
    def __init__(self) -> None:
        self.baseUrl = ' http://api.weatherapi.com/v1'
        self._key = 'ccdef128426f4c0a918131055220910'

    def getCurrentTemprature(self, city):
        response = requests.get(
            f'{self.baseUrl}/current.json?key={self._key}&q={city}')
        data = response.json()
        return data['current']['temp_c']

    def getTempratureAfter(self, city, days, hour=None):
        response = requests.get(
            f'{self.baseUrl}/forecast.json?key={self._key}&q={city}&days={days}&hour={hour}')
        data = response.json()
        # print(data)
        return data['forecast']['forecastday'][days-1]['day']['avgtemp_c']

    def getLatLong(self, city):
        response = requests.get(
            f'{self.baseUrl}/current.json?key={self._key}&q={city}')
        data = response.json()
        return data['location']['lat'], data['location']['lon']


w = WeatherAPI()
print(w.getLatLong('cairo'))
