from flask import Blueprint, jsonify, request #Import framework flask
from models import db, Comune #Import della classe Comune

comuni_blueprint = Blueprint('comuni_blueprint', __name__, url_prefix='/api/comuni') #Creazione di un blueprint per gestire le richieste dei comuni

#Recupera tutti i comuni del db
@comuni_blueprint.route('/', methods=['GET'])
def get_all_comuni():
    comuni = [] #Lista per il salvaraggio dei dizionari dei comuni recuperati
    comuni = Comune.query.all() #Recupero di tutti i comuni
    return jsonify([c.serialize() for c in comuni]) #Restituzione dei comuni in formato json

#Recupera un singolo comune in base all'ID
@comuni_blueprint.route('/<int:id>', methods=['GET'])
def get_comune(id):
    comune = Comune.query.get_or_404(id) #Recupera il comune o resituisce errore 404 se non esiste
    return jsonify(comune.serialize())

#Creazione di un nuovo comune
@comuni_blueprint.route('/', methods=['POST'])
def create_comune():
    try :
        data = request.json #Recupera i dati del comune dalla request sottoforma di dizionario (json)
        comune = Comune(**data) #Estrae dal dizionario i dati e crea l'oggetto comune
        db.session.add(comune) #Aggiunge l'oggetto comune al db
        db.session.commit()
        return jsonify(comune.serialize()), 201 #Restituzione del comune creato in formato json e con codice 201 "Created"
    except Exception as e:
        db.session.rollback() #Se si verifica un errore esegue il rollback della transazione
        return jsonify({"error" : str(e)}), 500 #Restituzione del errore in formato json e con codice 500 "Internal Server Error"

#Modifica di un comune in base all'ID
@comuni_blueprint.route('/<int:id>', methods=['PUT'])
def update_comune(id):
    try :
        comune = Comune.query.get_or_404(id) #Recupera il comune o resituisce errore 404 se non esiste
        data = request.json #Recupera i dati del comune dalla request sottoforma di dizionario (json)
        if ('id' in data.keys()):
            return { "error" : "Change id not possible" }, 404 #Non è possibile modificare l'ID
        for key, value in data.items():
            setattr(comune, key, value) #Aggiorna i valori del dizionario
        db.session.commit()
        return jsonify(comune.serialize())
    except Exception as e:
        db.session.rollback() #Se si verifica un errore esegue il rollback della transazione
        return jsonify({"error" : str(e)}), 500 #Restituisce errore 

#Eliminazione di un comune in base all'ID
@comuni_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_comune(id):
    comune = Comune.query.get_or_404(id) 
    db.session.delete(comune) #Elimina l'oggetto comune dal db
    db.session.commit()
    return '', 204 #Restituisco un codice 204 se l'eliminazione è andata a buon fine