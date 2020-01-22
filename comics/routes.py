from flask import render_template, url_for
from comics import app
from comics import requests

@app.route('/')
@app.route('/home')
def home():
     
     heroes = requests.get_superhero()
     print("Hello world",heroes)
     return render_template('home.html',heroes=heroes)
