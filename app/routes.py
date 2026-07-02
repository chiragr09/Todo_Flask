from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import AddTaskForm

@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Capybara"}
    todoList = [
        {
            'taskname': 'Write back to Anil',
            'completed': 'Yes'
        },
        {
            'taskname': 'Cook dinner',
            'completed': 'No'
        }
    ]
    return render_template('index.html', title='Home', user=user, todoList=todoList)

@app.route('/addtask', methods=['GET', 'POST'])
def addtask():
    form = AddTaskForm()
    if form.validate_on_submit():
        flash('Added the task successfully')
        return redirect(url_for('index'))
    return render_template('addtask.html', title='Add a task', form=form)
