from pymongo import MongoClient


class UserDAL:
    def __init__(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['users']
        self.collection = db.users

    def createUser(self, user_data):
        result = self.collection.insert_one(user_data)
        return result.inserted_id

    def findUserByEmail(self, email):
        return self.collection.find_one({"email": email})