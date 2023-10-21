from app import app
from app.controllers import task_controller, user_controller

if __name__ == '__main__':
    app.run(debug=True)