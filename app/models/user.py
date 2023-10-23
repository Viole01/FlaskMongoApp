from app import mongo

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        mongo.db.user.insert_one({
            "username": self.username,
            "password": self.password
        })
