import os

# config settings
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = os.environ['SECRET_KEY']

	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_LINK'] 
	SQLALCHEMY_TRACK_MODIFICATIONS = True 

class DevelopmentConfig(BaseConfig):
	DEBUG = True 
	

class ProductionConfig(BaseConfig):
	DEBUG = False 
