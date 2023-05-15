from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Email

class RegisterForm(FlaskForm):
    your_superhero_name = StringField('What Is Your Super Hero Name?!')
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Create Account')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class CollectionForm(FlaskForm):
    name = StringField("Name your hero you want to collect", validators=[DataRequired()])
    description = StringField('brief summary of the the hero')
    comics = StringField('how many comics did this hero apear in')
    superpower = StringField('does this superhero have any superpowers')
    submit = SubmitField('Submit')