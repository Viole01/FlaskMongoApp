from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

# Creating secret key
app.config["SECRET_KEY"] = "131de3c75a31705606da186f4fe0533f23ff66a8"
# Creating mongo uri
app.config["MONGO_URI"] = "mongodb+srv://prajjwalpawar1:DevServer@devserver.oog2xix.mongodb.net/?retryWrites=true&w=majority"

# Setup mongo
mongo = PyMongo(app)

from app import views
