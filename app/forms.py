from marshmallow import Schema, fields

class AddTaskForm(Schema):
    #Should be dump_only=True when integrating with mongo
    taskId = fields.Integer(required=True)
    taskname = fields.String(required=True)
    completed = fields.Boolean(load_default=False)

class UpdateTaskForm(Schema):
    taskId = fields.Integer(required=False)
    taskname = fields.String(required=False)
    completed = fields.Boolean(required=False)