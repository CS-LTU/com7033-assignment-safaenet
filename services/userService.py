import hashlib
from dal.usersDAL import create_user, get_user_by_email, update_user_password

# Takes password and argument and generates it's hash and returns it
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#Takes username and password, hashes the password and sends them to DAL to create a new user
def register_user(email, password):
    if get_user_by_email(email) is not None:
        return False
    hashed_pw = hash_password(password)
    create_user(email, hashed_pw)
    return True

# Takes username and password, hashes the password and combines them with the user credentials stored in the MongoDB
def authenticate_user(email, password):
    user = get_user_by_email(email)
    if user == None:
        return False
    elif user["password"] == hash_password(password):
        return True
    return False

# Takes username, old password and new password, searchs for user in the MongoDB to ckeck is it exists.
# Then checks if the old password is correct. Then updates the password to the new hashed password by sending them to DAL
def update_password(email, old_password, new_password):
    user = get_user_by_email(email)
    if user and user["password"] == hash_password(old_password):
        hashed_pw = hash_password(new_password)
        update_user_password(email, hashed_pw)
        return True
    return False
