'''
Created on Apr 20, 2020

@author: Jordan Barron
@version: April 20, 2020
'''
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from app.model.user import User
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)


@auth.route('/registration')
def registration():
    return render_template('registration.html')

@auth.route('/registration', methods = ['POST'])
def registration_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    
    if email and name and password:
        
        if len(password) < 8:
            flash('Password must be greater than 8 characters')
            return redirect(url_for('auth.registration'))
    
        user = db.users.get_user(email)

        if user: 
            flash('Email address already exists')
            return redirect(url_for('auth.registration'))

        user = User(email, name, generate_password_hash(password, method  = 'sha256'))
        db.users.add_user(user)    
        return redirect(url_for('auth.login'))
    
    flash('Missing data')
    return redirect(url_for('auth.registration'))

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods = ['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    
    if email and password:
        user = db.users.get_user(email)
    
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again')
            return redirect(url_for('auth.login'))
    
        login_user(user) 
        return redirect(url_for('main.my_events'))
    
    flash('Missing data')
    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required 
def logout():
    logout_user()
    return redirect(url_for('main.index'))
