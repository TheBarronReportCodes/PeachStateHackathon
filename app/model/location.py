'''
Created on Apr 23, 2020

@author: Jordan Barron
@version: April 23, 2020
'''
import json

class Location():
    def __init__(self, city, state, city_id):
        self.city = city
        self.state = state
        self.city_id = city_id

class Locations():
    def __init__(self):
        self.locations = []
        self.load()
    
    def load(self):
        locations = []
        try:
            with open("app/data/locations.json", "rt") as location_file:
                location_json_string = location_file.read()
                locations_wrapped = json.loads(location_json_string)
                locations = locations_wrapped["locations"]
        except:
            print("reading from locations.json failed")
            
        for location in locations:
            location_obj = Location(location["city"], location["state"], location["city_id"])
            self.locations.append(location_obj)
    
    def get_locations(self):
        return self.locations
    
    def get_location(self, city_id):
        for location in self.locations:
            if location.city_id == city_id:
                return location
            
        return None
            