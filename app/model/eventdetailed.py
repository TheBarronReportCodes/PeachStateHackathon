'''
Created on Apr 24, 2020

@author: Jordan Barron
@version: April 23, 2020
'''
class EventDetailed():
    def __init__(self, event_organizer, event_title, event_date, 
                 event_time, event_location_city, event_weather_condition, 
                 event_weather_description, event_weather_visual):
        self.event_organizer = event_organizer
        self.event_title = event_title
        self.event_date = event_date
        self.event_time = event_time
        self.event_location_city = event_location_city
        self.event_weather_condition = event_weather_condition
        self.event_weather_description = event_weather_description
        self.event_weather_visual = event_weather_visual       