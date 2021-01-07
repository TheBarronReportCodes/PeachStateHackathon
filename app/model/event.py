'''
Created on Apr 20, 2020

@author: Jordan Barron
@version: April 20, 2020
'''
import json

class Event():
    def __init__(self, email, name, date, time, location):
        self.email = email
        self.name = name
        self.date = date
        self.time = time
        self.location = location
        
class Events():
    def __init__(self):
        self.events = []
        self.load()
    
    def load(self):
        events = []
        try:
            with open("app/data/events.json", "rt") as event_file:
                event_json_string = event_file.read()
                events_wrapped = json.loads(event_json_string)
                events = events_wrapped["events"]
        except:
            print("reading from events.json failed")
        
        for event in events:
            event_obj = Event(event["email"], event["name"], event["date"], event["time"], event["location"])
            self.events.append(event_obj)
            
    def save(self):           
        events = []
        for event in self.events:
            event_dict = {"email": event.email, "name": event.name, "date": event.date, "time": event.time, "location": event.location}
            events.append(event_dict)
        
        try:
            with open("app/data/events.json", "wt") as event_file:
                event_file.write(json.dumps({"events": events}))
        except:
            print("writing to file events.json failed")
            return False
        
        return True
    
    def get_events(self, email=None):
        if not email:
            return self.events
        
        events = []
        for event in self.events:
            if event.email == email:
                events.append(event)
        return events   
            
    def get_event(self, event):
        for event in self.events:
            if event == event:
                return event
        
        return None
            
    def add_event(self, event):
        self.events.append(event)
        self.save()
    
    def delete_event(self, name):
        event_to_delete = None
        for event in self.events:
            if event.name == name:
                event_to_delete = event
        
        if event_to_delete:
            self.events.remove(event_to_delete)
            self.save()
