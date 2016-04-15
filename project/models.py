from project import db
from passlib.hash import sha256_crypt
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class UserInfo(db.Model):

	__tablename__ = "userinfo"

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(80), nullable=False)
	last_name = db.Column(db.String(80), nullable=False)
	email = db.Column(db.String, nullable=False, unique=True)
	password = db.Column(db.String, nullable=False)
	posts = relationship("Post", backref="author")

	def __init__(self, first_name, last_name, email, password):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = sha256_crypt.encrypt(str(password))

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def  __repr__(self):
		return '<first_name {} \n <last_name {}'.format(self.first_name, self.last_name)


class Post(db.Model):

	__tablename__ = "posts"

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, nullable=False)
	description = db.Column(db.String, nullable=False)
	author_id = db.Column(db.Integer, ForeignKey('userinfo.id'))

	def  __init__(self, title, description, author_id):
		self.title = title
		self.description = description
		self.author_id = author_id

	def __repr__(self):
		return '<title {}'.format(self.title)
