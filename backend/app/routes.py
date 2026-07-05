from flask import Response, request, jsonify
from app import app
from marshmallow import ValidationError
from bson import ObjectId
from app.database.db import mongo

@app.get("/tasks")
def get_tasks():
    todoList = list(mongo.db.tasks.find())
    for task in todoList:
        task["_id"] = str(task["_id"])
    return jsonify(todoList), 200

@app.post("/tasks")
def addtask():
    data = request.get_json()
    result = mongo.db.tasks.insert_one(data)
    return '', 200

@app.patch("/tasks/<task_id>")
def update_task(task_id):
    data = request.get_json()
    task = mongo.db.tasks.find_one({'_id': ObjectId(task_id)})
    if task is None:
        return jsonify({"error": "Task ID not found!"}), 404
    if 'taskname' in data:
        mongo.db.tasks.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": data}
        )
    if 'completed' in data:
        mongo.db.tasks.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": data}
        )
    return '', 200

@app.delete("/tasks/<task_id>")
def delete_task(task_id):
    try:
        print("Received task_id:", task_id)
        result = mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})
        if result.deleted_count == 0:
            return jsonify({"error": "Task not found"}), 404
        return "", 204
    except Exception as e:
        return jsonify({"Error": str(e)}), 400