from flask import Response, request, jsonify
from app import app
from marshmallow import ValidationError
from app.database.db import mongo

@app.get("/tasks")
def get_tasks():
    todoList = list(mongo.db.tasks.find({}, {'_id': 0}))
    return jsonify(todoList), 200

@app.post("/tasks")
def addtask():
    data = request.get_json()
    result = mongo.db.tasks.insert_one(data)
    return '', 200

@app.patch("/tasks/<int:task_id>")
def update_task(task_id):
    data = request.get_json()
    task = mongo.db.tasks.find_one({'taskId': task_id})
    if task is None:
        return jsonify({"error": "Task ID not found!"}), 404
    if 'taskId' in data:
        mongo.db.tasks.update_one(
            {"taskId": task_id},
            {"$set": data}
        )
    if 'taskname' in data:
        mongo.db.tasks.update_one(
            {"taskId": task_id},
            {"$set": data}
        )
    if 'completed' in data:
        mongo.db.tasks.update_one(
            {"taskId": task_id},
            {"$set": data}
        )
    return '', 200

@app.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    try:
        mongo.db.tasks.delete_one({"taskId": task_id})
    except:
        return jsonify({"Error": "Task ID not found"}), 404
    return '', 200