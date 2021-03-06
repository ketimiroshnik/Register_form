from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Login / email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Repeat password', validators=[DataRequired()])
    surname = StringField('Surname')
    name = StringField('Name')
    age = IntegerField("Age")
    position = StringField("Position")
    speciality = StringField("Speciality")
    address = StringField("Address")
    submit = SubmitField('Submit')
