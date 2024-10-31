from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["users"]
users = db["users"]

def get_user_by_email(email):
    user = users.find_one({"email": email})
    return user

def create_user(email, password):
    users.insert_one({"email": email, "password": password})

def update_user_password(email, new_password):
    users.update_one({"email": email}, {"$set": {"password": new_password}})
