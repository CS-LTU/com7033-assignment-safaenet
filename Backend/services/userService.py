from werkzeug.security import generate_password_hash, check_password_hash
from dal.usersDAL import UserDAL
from models.userModel import User

class UserService:
    def __init__(self):
        self.user_dal = UserDAL()

    def signup_user(self, email, password):
        if self.user_dal.findUserByEmail(email):
            return None, "User already exists"
        hashed_password = generate_password_hash(password)
        new_user = User(email=email, password=hashed_password)
        _id = self.user_dal.createUser(new_user.toDict())
        new_user._id = _id
        return new_user, None

    def login_user(self, email, password):
        user_data = self.user_dal.findUserByEmail(email)
        if not user_data:
            return None, "User not found"
        if not check_password_hash(user_data["password"], password):
            return None, "Incorrect password"
        return User.fromDict(user_data), None