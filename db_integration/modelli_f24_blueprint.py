from flask import Blueprint, jsonify, request #Import framework flask
from datetime import datetime #Import datetime
from models import db, ModelloF24, Impresa, Comune #Import models

modelli_f24_blueprint = Blueprint('modelli_f24_blueprint', __name__, url_prefix='/api/modellif24') #Creazione di un blueprint per gestire le richieste dei modelliF24

#Recupera tutti i modelliF24 nel db
@modelli_f24_blueprint.route('', methods=['GET'])
def get_all_modelli_f24():
    modelli_f24 = ModelloF24.query.all() #Recupero di tutti i modelliF24
    return jsonify([mf.serialize() for mf in modelli_f24]) #Restituzione di tutti i modelliF24 come json

#Recupera un singolo modelloF24 in base all'ID
@modelli_f24_blueprint.route('/<int:id>', methods=['GET'])
def get_modello_f24(id):
    modello_f24 = ModelloF24.query.get_or_404(id) #Recupero di un modelloF24 in base all'ID
    return jsonify(modello_f24.serialize())

#Creazione di un modelloF24
@modelli_f24_blueprint.route('/', methods=['POST'])
def create_modello_f24():
    try:
        data = request.json #Recupera i dati del comune dalla request sottoforma di dizionario (json)
        if ('impresa_id' in data.keys() and 'comune_id' in data.keys() and 'data' in data.keys()):
            impresa_id = data.pop('impresa_id') #Recupera l'ID dell'impresa dal dizionario e poi lo cancella dal dizionario
            comune_id = data.pop('comune_id') #Recupera l'ID del comune dal dizionario e poi lo cancella dal dizionario
            impresa = Impresa.query.get_or_404(impresa_id) #Recupera l'oggeto Impresa legato all'ID
            comune = Comune.query.get_or_404(comune_id) #Recupera l'oggeto Comune legato all'ID
            modello_f24 = ModelloF24(impresa=impresa, **data) #Creazione di un nuovo modelloF24
            comune.modelli_f24_emessi.append(modello_f24) #Registra l'emissione del modelloF24 nel comune
            db.session.add(modello_f24) #Aggiunge l'oggetto modelloF24 al db
            db.session.commit()
            return jsonify(modello_f24.serialize()), 201
        else:
            return { 'error' : "Missing parameters" }, 400 #Se non sono presenti i parametri richiesti ritorna un errore 400
    except Exception as e:
        db.session.rollback() #Se si verifica un errore esegue il rollback della transazione
        return jsonify({"error" : str(e)}), 500
     
#Modifica di un modelloF24 in base all'ID
@modelli_f24_blueprint.route('/<int:id>', methods=['PUT'])
def update_modello_f24(id):
    try:
        modello_f24 = ModelloF24.query.get_or_404(id) #Recupero di un modelloF24 in base all'ID
        data = request.json #Recupera i dati del modelloF24 dalla request sottoforma di dizionario (json)
        if ('impresa_id' in data.keys()):
            return {"error" : "Change impresa not possible"}, 400 #Non è possibile modificare l'ID impresa
        if ('comune_id' in data.keys()):
            return {"error" : "Change comune not possible"}, 400 #Non è possibile modificare l'ID comune
        for key, value in data.items():
            if (key == 'data'):
                setattr(modello_f24, key, datetime.strptime(value, "%Y-%m-%d")) #Converte la data in un oggetto datetime
            else:
                setattr(modello_f24, key, value) #Aggiorna i valori del dizionario
        db.session.commit()
        return jsonify(modello_f24.serialize())
    except Exception as e:
        db.session.rollback() #Se si verifica un errore esegue il rollback della transazione
        return jsonify({"error" : str(e)}), 500 #Restituisce errore 

#Eliminazione di un modelloF24 in base all'ID
@modelli_f24_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_modello_f24(id):
    modello_f24 = ModelloF24.query.get_or_404(id)
    db.session.delete(modello_f24) #Eliminazione del modelloF24
    db.session.commit()
    return '', 204 #Restituisce un codice 204 se l'eliminazione è andata a buon fine

#Preparazione di un modelloF24 in base all'ID
@modelli_f24_blueprint.route('/<int:id>/prepara', methods=['GET'])
def prepara_modello_f24(id):
    modello_f24 = ModelloF24.query.get_or_404(id)
    return modello_f24.prepara_f24()