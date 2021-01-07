'''
Created on Apr 20, 2020

@author: Jordan Barron
@version: April 20, 2020
'''
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from . import db
from app.model.event import Event
from app.model.eventdetailed import EventDetailed
from app.model.myeventdetailed import MyEventDetailed
from random import randint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    random_fun_fact = db.funfact.get_funfact(randint(1, 10)).fact
    
    events = db.events.get_events()
    
    detailed_events = []
    
    for event in events:
        event_organizer = event.email
        event_title = event.name
        event_date = event.date
        event_time = event.time
        
        location = db.location.get_location(event.location)
        event_location_city = location.city
        event_location_city_id = location.city_id

        event_weather_condition = db.weather.get_weather(event_location_city_id).condition
        event_weather_description = db.weather.get_weather(event_location_city_id).description
        
        if (event_weather_condition == 'Thunderstorm'):
            event_weather_visual  = 'https://cdn.britannica.com/s:800x450,c:crop/52/22452-138-1B738483/thunderstorm-updraft-cumulonimbus-cloud-air.jpg'
        elif(event_weather_condition == 'Rain'):
            event_weather_visual  = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTMOjFTvd6eJcQ_6tv7pfomLvQifEZ7RabAGRdLydimrA7zOveq&usqp=CAU'
        elif(event_weather_condition == 'Clouds'):
            event_weather_visual  = 'https://images.unsplash.com/photo-1501630834273-4b5604d2ee31?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=500&q=80'
        elif(event_weather_condition == 'Fog'):
            event_weather_visual  = 'https://images.unsplash.com/photo-1485236715568-ddc5ee6ca227?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=500&q=80'
        else:
            event_weather_visual = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQUJiN2arRFde36EOc72ki868cMPui6VBEsm8-0TuSnrkNRx0Dv&usqp=CAU'
        
        event_detailed_obj = EventDetailed(event_organizer, event_title, 
                                           event_date, event_time, 
                                           event_location_city, event_weather_condition, 
                                           event_weather_description, event_weather_visual)
        detailed_events.append(event_detailed_obj)
        
    return render_template('index.html', detailed_events = detailed_events, random_fun_fact = random_fun_fact)

@main.route('/my-events')
@login_required
def my_events():
    random_fun_fact = db.funfact.get_funfact(randint(1, 10)).fact
    
    myevents = db.events.get_events(current_user.email)
    detailed_my_events = []
    
    for event in myevents:
        my_event_title = event.name
        my_event_date = event.date
        my_event_time = event.time
        
        location = db.location.get_location(event.location)
        my_event_location_city = location.city
        
        my_event_detailed_obj = MyEventDetailed(my_event_title, my_event_date, my_event_time,
                                                my_event_location_city)
        detailed_my_events.append(my_event_detailed_obj)
    
    return render_template('myevents.html', name = current_user.name, detailed_my_events = detailed_my_events, random_fun_fact = random_fun_fact)
    
@main.route('/add')
@login_required  
def add_events_form():
    random_fun_fact = db.funfact.get_funfact(randint(1, 10)).fact
    locations = db.location.get_locations()
    return render_template('add_events_form.html', locations = locations, random_fun_fact = random_fun_fact)

@main.route('/add', methods = ['POST'])
@login_required
def add_events():
    name = request.form.get('name')
    date = request.form.get('date')
    hour = request.form.get('hour')
    minutes = request.form.get('minutes')
    location = request.form.get('location')
    
    if name and date and hour and minutes and location: 
        
        #create time variable
        hour_int = int(hour)
        minutes_int = int(minutes)
        if hour_int < 10:
            hour = '0' + hour
        if minutes_int < 10:
            minutes = '0' + minutes
        time = (hour + ':' + minutes + ' ')

        event = Event(current_user.email, name, date, time, location)
        db.events.add_event(event) 
        return redirect(url_for('main.my_events'))
    
    flash('One or more of the fields are empty')
    return redirect(url_for('main.add_events_form'))


@main.route('/delete', methods = ['POST'])
@login_required
def delete_event():
    try:
        name = request.form.get('name')
        db.events.delete_event(name)
        return redirect(url_for('main.my_events'))
    except:
        print('error')