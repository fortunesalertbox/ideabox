from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# login form populated by flask wtform
class LoginForm(Form):
	email = TextField('Email', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])

# registration form populated by flask wtform
class RegistrationForm(Form):
	first_name = TextField(
		'first_name',
		validators=[DataRequired(),Length(min=3, max=25)]
	)
	last_name=TextField(
		'last_name',
		validators=[DataRequired(),Length(min=3, max=25)]
	)
	email = TextField(
		'email',
		validators=[DataRequired(),  Email(message=None), Length(min=6, max=40)]
	)
	password = PasswordField(
		'password',
		validators=[DataRequired(), Length(min=6, max=25)]
	)
	confirm = PasswordField(
		'Repeat Password',
		validators=[
			DataRequired(), EqualTo('password', message='Password must match.')
		]
	)