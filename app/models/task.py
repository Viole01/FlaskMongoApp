from app import mongo

class Task:
    def __init__(self, name, description, assigned_userID):
        self.name = name
        self.description = description
        self.assigned_userID = assigned_userID

    def save(self):
        mongo.db.tasks.insert_one({
            "name": self.name,
            "description": self.description,
            "assigned_userID": self.assigned_userID
        })