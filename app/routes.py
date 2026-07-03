from flask import jsonify, request
from app import app
from app.forms import AddTaskForm, UpdateTaskForm
from marshmallow import ValidationError

tasks = [
    {
        "taskId": 1,
        "taskname": "Write back to Anil",
        "completed": True
    },
    {
        "taskId": 2,
        "taskname": "Cook dinner",
        "completed": False
    }
]

schema = AddTaskForm()
update_schema = UpdateTaskForm()

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

@app.patch("/tasks/<int:task_id>")
def update_task(task_id):
    data = request.get_json()
    try:
        updates = update_schema.load(data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    for task in tasks:
        if task["taskId"] == task_id:
            task.update(updates)
            return jsonify(task), 200

    return jsonify({"error": "Task ID not found"}), 404

@app.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    for task in tasks:
        if task["taskId"] == task_id:
            tasks.remove(task)
            return '', 204

    return jsonify({"error": "Task ID not found"}), 404