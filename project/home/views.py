##################
#### Imports #####
##################

from project import app, db
from project.models import UserInfo, Post
from flask import flash, redirect, request, url_for, \
	render_template, Blueprint
from flask.ext.login import login_required, current_user
#from functools import wraps

from form import MessageForm

################
#### config ####
################

home_blueprint = Blueprint(
	'home', __name__,
	template_folder='templates'
)

# This helper function is just sticking around for a while
"""
##########################
#### helper functions ####
##########################

def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('welcome'))
	return wrap 
"""
############
## Routes ##
############


@home_blueprint.route('/', methods=['GET', 'POST'])
@home_blueprint.route('/index')
@login_required
def index():
	error = None
	form = MessageForm(request.form)
	if form.validate_on_submit():
		new_idea = Post(
			form.title.data,
			form.description.data,
			current_user.id
		)
		db.session.add(new_idea)
		db.session.commit()
		flash('New Idea Shared!')
		return redirect(url_for('home.index'))
	else:
		posts = db.session.query(Post).order_by('posts.id desc')
	first_name = current_user.first_name
	last_name = current_user.last_name
	return render_template(
		'index.html', posts=posts, 
		form=form, error=error, 
		last_name=last_name, first_name=first_name,
		title="Home"
	)


@home_blueprint.route('/welcome')
def welcome():
	return render_template('welcome.html', title="Welcome")
