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
        return False
    elif user["password"] == hash_password(password):
        return True
    return False

def update_password(email, old_password, new_password):
    user = get_user_by_email(email)
    if user and user["password"] == hash_password(old_password):
        hashed_pw = hash_password(new_password)
        update_user_password(email, hashed_pw)
        return True
    return False
