from marshmallow import Schema, fields

class AddTaskForm(Schema):
    taskname = fields.String(required=True)
    completed = fields.Boolean(load_default=False)