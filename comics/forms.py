from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,PasswordField, SubmitField, BooleanField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError



class LoginForm(FlaskForm):
    
    email = StringField ('Email', validators = [DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content =TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Sign Up')
    
    def validate_username(self,username):
            
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username is already taken. Choose a different one')
         
    def validate_email(self, email):
       
            email=User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('Email is already taken. Choose a different one')
class UpdateForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
   
    submit = SubmitField('Update')
     
    def validate_username(self, username):
        if username.data != current_user.username:
            
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username is already taken. Choose a different one')
         
    def validate_email(self, email):
         if email.data != current_user.email: 
         
            email=User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('Email is already taken. Choose a different one')