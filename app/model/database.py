'''
Created on Mar 25, 2020

@author: CS6252
'''
from app.model.user import Users
from app.model.event import Events
from app.model.weather import LocationInfo
from app.model.location import Locations
from app.model.funfact import FunFacts

class Database:
    
    def __init__(self):
        self.events = Events()
        self.users = Users()
        self.weather = LocationInfo()
        self.location = Locations()
        self.funfact = FunFacts()
        