# PeachStateHackathon
SIGN IN: emailAddress: employer@company.me ; password: employer@company.me

Database-driven Python web application that displays hackathons occurring in the ten largest Georgia cities

###Task

Users can register and login to the site. An authencated user can post events and delete their events. Any website visitor can view all posted events.

##Criteria

A home page, a Login page, a registration page, and a my-events page, where an authencated user can add and delete their events. MVC standard. Data used for events JSON, user JSON, funfacts JSON, weatherAPI. Model used to store User object, Event object, FunFacts object, and Weather object. View used to display base page, index, my events, login, and registration. Controller used to provide database initiation, as well as control of authentication and the index.

##Summary of Tech Stack JSON used to control data, Flask used to authenticate a user, track the user, and set up jinja template for HTML. Python used as main backend language

##Functionality Authentication functionaity uses Cookie-based authencationon using Flask-Login. Once logged in, functionality involves flash messaging for validation errors, requests to retrieve form data, and Post and Get to display data from the JSON files
