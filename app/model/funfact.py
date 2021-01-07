'''
Created on Apr 24, 2020

@author: Jordan Barron
@version: April 24, 2020
'''
import json

class FunFact():
    def __init__(self, number, fact):
        self.number = number
        self.fact = fact

class FunFacts():
    def __init__(self):
        self.funfacts = []
        self.load()
        
    def load(self):
        funfacts = []
        try:
            with open("app/data/funfacts.json", "rt") as funfacts_file:
                funfact_json_string = funfacts_file.read()
                funfacts_wrapped = json.loads(funfact_json_string)
                funfacts = funfacts_wrapped["funfacts"]
        except:
            print("reading from funfacts.json failed")
            
        for funfact in funfacts:
            funfact_obj = FunFact(funfact["number"], funfact["fact"])
            self.funfacts.append(funfact_obj)
    
    def get_funfacts(self):
        return self.funfacts
    
    def get_funfact(self, number):
        for funfact in self.funfacts:
            if funfact.number == number:
                return funfact
        
        return None
        