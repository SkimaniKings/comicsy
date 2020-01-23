from flask import render_template, url_for, flash, redirect, request
from comics import app, db, bcrypt
from comics.forms import RegistrationForm
from comics.models import User, Post




@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
    heroes = requests.get_superhero()
     
    return render_template('home.html',heroes=heroes)




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
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

