from flask import jsonify, request
from app import app
from app.forms import AddTaskForm
from marshmallow import ValidationError

tasks = [
    {
        "taskname": "Write back to Anil",
        "completed": True
    },
    {
        "taskname": "Cook dinner",
        "completed": False
    }
]

schema = AddTaskForm()

@app.get("/tasks")
def get_tasks():
    response = {
      "user": {
        "username":"Capybara"
      },
      "todoList": tasks
    }
    return jsonify(response)

@app.post("/tasks")
def addtask():
    data = request.get_json()
    try:
        task = schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 401
    tasks.append(task)
    return jsonify(task), 201
