from flask import render_template, url_for, flash, redirect
from comics import app
from comics.forms import RegistrationForm



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)