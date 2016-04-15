from app import db
from models import UserInfo

# insert data
db.session.add(UserInfo("fortune", "iyke", "legalmody@gmail.com", "test123"))
db.session.add(UserInfo("onyii", "gift", "ike4tune@gmail.com", "pword123"))

db.session.commit()