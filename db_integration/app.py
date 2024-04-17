from flask import Flask #Import framework flask
from comuni_blueprint import comuni_blueprint 
from imprese_blueprint import imprese_blueprint
from modelli_f24_blueprint import modelli_f24_blueprint
from models import db #Importazione del database

app = Flask(__name__) #Creazione dell'applicazione

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #Creazione della connessione al database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Disabilitazione delle notifiche di SQLAlchemy

db.init_app(app) #Creazione della connessione al database

#Registro dei blueprint delle API
app.register_blueprint(comuni_blueprint)
app.register_blueprint(imprese_blueprint)
app.register_blueprint(modelli_f24_blueprint)

with app.app_context(): #Creazione della tabella del database
    db.create_all() 