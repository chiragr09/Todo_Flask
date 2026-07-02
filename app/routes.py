from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
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
