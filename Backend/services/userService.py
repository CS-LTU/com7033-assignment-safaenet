# from werkzeug.security import generate_password_hash, check_password_hash
# from dal.usersDAL import UserDAL
# from models.userModel import User

# class UserService:
#     salt = "1q2w3e4r"
    
#     def __init__(self):
#         self.user_dal = UserDAL()

#     def signup_user(self, email, password):
#         if self.user_dal.findUserByEmail(email):
#             return None, "User already exists"
#         hashed_password = generate_password_hash(password + self.salt)
#         new_user = User(email=email, password=hashed_password)
#         _id = self.user_dal.createUser(new_user.toDict())
#         new_user._id = _id
#         return new_user, None

#     def login_user(self, email, password):
#         user_data = self.user_dal.findUserByEmail(email)
#         if not user_data:
#             return None, "User not found"
#         if not check_password_hash(user_data["password"], password + self.salt):
#             return None, "Incorrect password"
#         return User.fromDict(user_data), None

import hashlib
from dal.usersDAL import create_user, get_user_by_email, update_user_password

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(email, password):
    if get_user_by_email(email) is not None:
        return False
    hashed_pw = hash_password(password)
    create_user(email, hashed_pw)
    return True

def authenticate_user(email, password):
    user = get_user_by_email(email)
    if user == None:
        return "UserNotFound"
    if user and user["password"] == hash_password(password):
        return True
    return False

def update_password_service(email, old_password, new_password):
    user = get_user_by_email(email)
    if user and user["password"] == hash_password(old_password):
        hashed_pw = hash_password(new_password)
        update_user_password(email, hashed_pw)
        return True
    return False
