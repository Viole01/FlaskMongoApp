from flask import render_template
from app.models.user import User

def register_user(username, password):
    user = User(username, password)
    user.save()
    return render_template('user_profile.html', user=user)