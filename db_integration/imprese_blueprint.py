from datetime import datetime #Import datetime
from flask import Blueprint, jsonify, request #Import framework flask
from models import db, Impresa, Comune #Import models

imprese_blueprint = Blueprint('imprese_blueprint', __name__, url_prefix='/api/imprese') #Creazione di un blueprint per gestire le richieste delle imprese

#Recupera tutte le imprese nel db
@imprese_blueprint.route('/', methods=['GET'])
def get_all_imprese():
    imprese = Impresa.query.all() #Recupero tutte le imprese 
    return jsonify([imp.serialize() for imp in imprese]) #Restituzione di tutte le imprese in formato json

#Recupera una singola impresa in base all'ID
@imprese_blueprint.route('/<int:id>', methods=['GET'])
def get_impresa(id):
    impresa = Impresa.query.get_or_404(id) #Recupero di un'impresa in base all'ID
    return jsonify(impresa.serialize())

#Creazione di una nuova impresa
@imprese_blueprint.route('/', methods=['POST'])
def create_impresa():
    try :
        data = request.json #Recupera i dati del comune dalla request sottoforma di dizionario (json)
        comune_id = None 
        if ('comune_id' in data.keys()):
            comune_id = data.pop('comune_id') #Recupera l'ID del comune dal dizionario e poi lo cancella dal dizionario
        impresa = Impresa(**data) #Estrae dal dizionario i dati e crea l'oggetto impresa
        if (comune_id != None):
            comune = Comune.query.get_or_404(comune_id)
            comune.imprese_registrate.append(impresa) #Registra l'impresa nel comune
        db.session.add(impresa) #Aggiunge l'oggetto impresa al db
        db.session.commit()
        return jsonify(impresa.serialize()), 201
    except Exception as e:
        db.session.rollback() #Se si verifica un errore esegue il rollback della transazione
        return jsonify({"error" : str(e)}), 500 #Restituisce errore 

#Modifica di un'impresa in base all'ID
@imprese_blueprint.route('/<int:id>', methods=['PUT'])
def update_impresa(id):
    try:
        impresa = Impresa.query.get_or_404(id) 
        data = request.json #Recupera i dati del comune dalla request sottoforma di dizionario (json)
        comune_id = data.pop('comune_id') #Recupera l'ID del comune dal dizionario e poi lo cancella dal dizionario
        if (impresa.comune_id != None):
            comune = Comune.query.get_or_404(impresa.comune_id)
            comune.imprese_registrate.remove(impresa) #Rimuove la registrazione dell'impresa dal comune 
        if (comune_id != None):
            comune = Comune.query.get_or_404(comune_id)
            comune.imprese_registrate.append(impresa) #Registra l'impresa nel comune
        for key, value in data.items():
            if (key == "data_costituzione"):
                value = datetime.strptime(value, "%Y-%m-%d") #Converte la data in un oggetto datetime
            setattr(impresa, key, value) #Aggiorna i valori del dizionario
        db.session.commit() 
        return jsonify(impresa.serialize()) 
    except Exception as e:
        db.session.rollback() #Se si verifica un errore esegue il rollback della transazione
        return jsonify({"error" : str(e)}), 500 #Restituisce errore 

#Eliminazione di un'impresa in base all'ID
@imprese_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_impresa(id):
    impresa = Impresa.query.get_or_404(id)
    db.session.delete(impresa) #Elimina l'impresa dal db
    db.session.commit()
    return '', 204 #Restituisce un codice 204 se l'eliminazione è andata a buon fine
