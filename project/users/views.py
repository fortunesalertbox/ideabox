##################
#### Imports #####
##################

from flask import flash, redirect, render_template, request, \
	session, url_for, Blueprint
#from functools import wraps 
from flask.ext.login import login_user, \
    login_required, logout_user 

from forms import LoginForm, RegistrationForm
from project import db
from project.models import UserInfo, Post, sha256_crypt

##################
#### Config ######
##################

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)

############
## Routes ##
############

@users_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
	error=None
	form=RegistrationForm()
	if form.validate_on_submit():
		user=UserInfo(
			first_name=form.first_name.data,
			last_name=form.last_name.data,
			email=form.email.data,
			password=form.password.data
		)
		db.session.add(user)
		db.session.commit()
		login_user(user)
		#session['logged_in'] = True 
		return redirect(url_for('home.index'))
	return render_template('signup.html', 
		form=form, error=error, 
		title='Register'
	)


# route for handling the login page logic
@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	form = LoginForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			user = UserInfo.query.filter_by(
				email=request.form['email']
			).first()
			if user is not None and \
					sha256_crypt.verify(
						str(request.form['password']), 
						user.password
					):
				#session['logged_in'] = True 
				login_user(user)
				flash('login successful')
				return redirect(url_for('home.index'))
			else:
				error = 'The Email or Password you entered maybe wrong. Please try again'
	return render_template('login.html', form=form, error=error, title='Login')


@users_blueprint.route('/logout')
@login_required
def logout():
	#session.pop('logged_in', None)
	logout_user()
	flash('You\'ve been logged out.')
	return redirect(url_for('home.welcome'))
