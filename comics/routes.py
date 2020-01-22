<<<<<<< HEAD
from flask import render_template, url_for, flash, redirect
from comics import app, bcrypt, db
from comics.forms import RegistrationForm
from comics.models import User


=======
from flask import render_template, url_for, flash, redirect, request
from comics import app
>>>>>>> bec7e2a786403b83a749abbb1fb7430c3cf5c074

from comics.forms import LoginForm


from comics import requests


@app.route('/')
@app.route('/home')
def home():

    return render_template('home.html')


<<<<<<< HEAD

@app.route("/register", methods=['GET', 'POST'])
def register():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
=======
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
     
     heroes = requests.get_superhero()
     print("Hello world",heroes)
     return render_template('home.html',heroes=heroes)
>>>>>>> bec7e2a786403b83a749abbb1fb7430c3cf5c074
