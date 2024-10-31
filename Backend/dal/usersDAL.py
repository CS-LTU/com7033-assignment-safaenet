# from pymongo import MongoClient


# class UserDAL:
#     def __init__(self):
#         client = MongoClient('mongodb://localhost:27017/')
#         db = client['users']
#         self.collection = db.users

#     def createUser(self, user_data):
#         result = self.collection.insert_one(user_data)
#         return result.inserted_id

#     def findUserByEmail(self, email):
#         return self.collection.find_one({"email": email})

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
