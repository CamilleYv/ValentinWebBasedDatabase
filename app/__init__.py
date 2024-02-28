from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
# Configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///LeValentin.db'
db = SQLAlchemy(app)

# Import models after the db object is created to avoid circular imports
from app.models import RawMaterial, Recipe

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db, 
        'RawMaterial': RawMaterial, 
        'Recipe': Recipe
    }
