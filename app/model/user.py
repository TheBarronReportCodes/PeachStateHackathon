'''
Created on Apr 20, 2020

@author: Jordan Barron
@version: April 20, 2020
'''
import json
from flask_login.mixins import UserMixin

class User(UserMixin):
    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password
    
    def get_id(self):
        return self.email

class Users:
    def __init__(self):
        self.users = []
        users = []
        try:
            with open("app/data/users.json", "rt") as user_file:
                users_json_string = user_file.read()
                users_wrapped = json.loads(users_json_string)
                users = users_wrapped["users"]
        except:
            print("reading from users.json failed")
        
        for user in users:
            user_obj = User(user["email"], user["name"], user["password"])
            self.users.append(user_obj)
    def get_users(self):
        return self.users
            
    def get_user(self, email):
        for user in self.users:
            if user.email == email:
                return user
            
        return None    
        
    def add_user(self, user):
        self.users.append(user)
        
        users = []
        for user in self.users:
            user_dict = {"email": user.email, "name": user.name, "password": user.password}
            users.append(user_dict)
            
        try:
            with open("app/data/users.json", "wt") as user_file:
                user_file.write(json.dumps({"users": users}))
        except:
            print("writing to file users.json failed")
            return False
        
        return True