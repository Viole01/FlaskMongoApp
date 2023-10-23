from app import app
from flask import render_template

from app.controllers.user_controller import register_user

@app.route('/')
def homepage():
    return render_template('homepage.html', title='Homepage')


@app.route('/user_profile')
def main():
    return register_user(username, password)