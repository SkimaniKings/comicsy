from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
<<<<<<< HEAD
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
=======

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
>>>>>>> bec7e2a786403b83a749abbb1fb7430c3cf5c074


from comics import routes