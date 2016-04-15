import os

# config settings
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = '`\x82\x99\xc2\xd5=\xdeJ\xd4\xb9\xb9\xf1O\x96\
		x0f\xe7\xfa\x91\x95\xc0\x04\x8aW\x99'

	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_LINK'] 
	SQLALCHEMY_TRACK_MODIFICATIONS = True 

class DevelopmentConfig(BaseConfig):
	DEBUG = True 
	

class ProductionConfig(BaseConfig):
	DEBUG = False 
