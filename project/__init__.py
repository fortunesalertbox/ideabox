##################
#### Imports #####
##################

from flask import Flask 
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
import os

##################
#### Config ######
##################

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)


from project.users.views import users_blueprint
from project.home.views import home_blueprint

# register the blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)

from models import UserInfo

login_manager.login_view = "users.login"


@login_manager.user_loader
def load_user(user_id):
    return UserInfo.query.filter(UserInfo.id == int(user_id)).first()
