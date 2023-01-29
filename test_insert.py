#Testing file for integration between controller and data model

from controller.user import User
from model.handle_db import HandleDB

data={
    "UserName":"Jhon",
    "Password":"123456789",
}
user= User(data);
db=HandleDB();

user.create_user();

print(db.get_all());