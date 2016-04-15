from project import db
from project.models import UserInfo, Post

#create the db and the db tables
db.create_all()

#insert data into it
db.session.add(UserInfo('fortune', 'iyke', 'legalmody@gmail.com', 'test123'))
#db.session.add(UserInfo('ikechukwu', 'ekeruo', 'fortune_ik@yahoo.com', '123test'))

db.session.add(Post('First Idea Shared', 
		'This is the first Idea ever shared on Ideabox, I hope you find that cool',
		1
	)
)

# commit the changes
db.session.commit()