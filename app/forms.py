from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms. validators import DataRequired

class AddTaskForm(FlaskForm):
    taskname = StringField('Add a task', validators=[DataRequired()])
    submit = SubmitField('Add!')
