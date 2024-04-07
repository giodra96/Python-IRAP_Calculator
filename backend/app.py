from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from comuni_blueprint import comuni_blueprint
from imprese_blueprint import imprese_blueprint
from modelli_f24_blueprint import modelli_f24_blueprint
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db.init_app(app)

# Registro dei blueprint delle API
app.register_blueprint(comuni_blueprint)
app.register_blueprint(imprese_blueprint)
app.register_blueprint(modelli_f24_blueprint)

with app.app_context():
    db.create_all()