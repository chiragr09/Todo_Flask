from flask import Flask
from config import Config
from flask_cors import CORS
from app.database.db import initialize_db

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

app.config["MONGO_URI"] = "mongodb://localhost/TodoApp"
initialize_db(app)

from app import routes
