##################
#### Imports #####
##################

from project import app, db
from project.models import UserInfo, Post
from flask import flash, redirect, request, url_for, \
	render_template, Blueprint
from flask.ext.login import login_required, login_user, \
	logout_user, current_user


from form import MessageForm

################
#### config ####
################

home_blueprint = Blueprint(
	'home', __name__,
	template_folder='templates'
)

############
## Routes ##
############

@home_blueprint.route('/index', methods=['GET', 'POST'])
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


@home_blueprint.route('/')
@home_blueprint.route('/welcome')
def welcome():
	return render_template('welcome.html', title="Welcome")


@home_blueprint.route('/upvote', methods=['GET', 'POST'])
def upvote():
	pass

@home_blueprint.route('/downvote')
def downvote():
	pass
