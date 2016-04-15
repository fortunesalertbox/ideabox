from app import db
from models import UserInfo

#create the db and the db tables
db.create_all()

#insert data into it
db.session.add(UserInfo('fortune', 'iyke', 'legalmody@gmail.com', 'test123'))
db.session.add(UserInfo('ikechukwu', 'ekeruo', 'fortune_ik@yahoo.com', '123test'))


# commit the changes
db.session.commit()