'''
Created on Apr 23, 2020

@author: Jordan Barron
@version: April 23, 2020
'''
import requests

class Weather():
    def __init__(self, condition, description):
        self.condition = condition
        self.description = description

class LocationInfo():    
    def get_weather(self, location):
        try:
            url = 'http://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid=81c1c50f034c360d7e388f0582b62746'.format(location)
            weather = requests.get(url)
            weather_wrapped = weather.json()
            weather = weather_wrapped["weather"]
        except:
            print("loading this api failed")
        
        for data in weather:
            weather_obj = Weather(data['main'], data['description'])
        return weather_obj
