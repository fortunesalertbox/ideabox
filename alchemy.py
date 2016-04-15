from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://legal:lagelmody@85.10.205.173/users_db_' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Example(db.Model):

	__tablename__ = 'example'
	
	id = db.Column('id', db.Integer, primary_key=True)
	data = db.Column('data', db.Unicode)