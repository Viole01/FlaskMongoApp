from flask import render_template
from app.models.task import Task

def create_task(title, description, assigned_userID):
    task = Task(title, description, assigned_userID)
    task.save()
    return render_template("task_list.html", task=task)