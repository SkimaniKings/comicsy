
import os
import secrets
from flask import render_template, url_for, flash, redirect,request,abort
from comics import app, db, bcrypt
from comics.models import User
from comics.forms import RegistrationForm, LoginForm
from flask_login import login_user,current_user,logout_user,login_required
from comics import requests


@app.route('/home')
def home():
     heroes = requests.get_superhero()
     return render_template('home.html',heroes=heroes)
 
@app.route('/index')
@app.route('/')
def index():
    
     return render_template('index.html')
 
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password= bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        
        flash(
            f'You have successfully created an account for {form.username.data}! You can now log in to your account','success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
         
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. please confirm email and password.','danger')
    
    return render_template('login.html', form=form)

@app.route("/articles", methods=['GET', 'POST'])  
def articles():
  
    return render_template('articles.html' )

@app.route("/contacts", methods=['GET', 'POST'])  
def contacts():
  
    return render_template('contacts.html' )
@app.route("/about", methods=['GET', 'POST'])  
def about():
  

    return render_template('profile.html', title='Profile' ,form=form)
     
