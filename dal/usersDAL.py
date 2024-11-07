from pymongo import MongoClient

# Nessecary configurations to connect to the MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["users"]
users = db["users"]

# Takes the username (email) as argument and searchs for the user in MongoDB
def get_user_by_email(email):
    user = users.find_one({"email": email})
    return user

# Gets email and hashed password and then stores them in MongoDB
def create_user(email, password):
    users.insert_one({"email": email, "password": password})

# Gets the email and hashed passwords and updates the password of the user in MongoDB
def update_user_password(email, new_password):
    users.update_one({"email": email}, {"$set": {"password": new_password}})