from project import db
from project.models import UserInfo, Post

# insert data
db.session.add(UserInfo("fortune", "iyke", "legalmody@gmail.com", "test123"))
db.session.add(UserInfo("onyii", "gift", "ike4tune@gmail.com", "pword123"))

db.session.commit()