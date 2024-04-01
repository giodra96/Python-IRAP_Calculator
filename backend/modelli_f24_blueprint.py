from flask import Blueprint, jsonify, request
from datetime import datetime
from models import db, ModelloF24, Impresa, Comune  # Assicurati di importare i modelli necessari

modelli_f24_blueprint = Blueprint('modelli_f24_blueprint', __name__, url_prefix='/api/modellif24')

# Gestione dei ModelliF24
@modelli_f24_blueprint.route('', methods=['GET'])
def get_all_modelli_f24():
    modelli_f24 = ModelloF24.query.all()
    return jsonify([mf.serialize() for mf in modelli_f24])

@modelli_f24_blueprint.route('/<int:id>', methods=['GET'])
def get_modello_f24(id):
    modello_f24 = ModelloF24.query.get_or_404(id)
    return jsonify(modello_f24.serialize())

@modelli_f24_blueprint.route('/', methods=['POST'])
def create_modello_f24():
    try:
        data = request.json
        if ('impresa_id' in data.keys() and 'comune_id' in data.keys() and 'data' in data.keys()):
            impresa_id = data.pop('impresa_id')
            comune_id = data.pop('comune_id')
            impresa = Impresa.query.get_or_404(impresa_id)
            comune = Comune.query.get_or_404(comune_id)
            modello_f24 = ModelloF24(impresa=impresa, **data)
            comune.modelli_f24_emessi.append(modello_f24)
            db.session.add(modello_f24)
            db.session.commit()
            return jsonify(modello_f24.serialize()), 201
        else:
            return { 'error' : "Missing parameters" }, 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error" : str(e)}) , 500
     

@modelli_f24_blueprint.route('/<int:id>', methods=['PUT'])
def update_modello_f24(id):
    try:
        modello_f24 = ModelloF24.query.get_or_404(id)
        data = request.json
        if ('impresa_id' in data.keys()):
            return {"error" : "Change impresa not possible"}, 400
        if ('comune_id' in data.keys()):
            return {"error" : "Change comune not possible"}, 400
        for key, value in data.items():
            if (key == 'data'):
                setattr(modello_f24, key, datetime.strptime(value, "%Y-%m-%d"))    
            else:
                setattr(modello_f24, key, value)
        db.session.commit()
        return jsonify(modello_f24.serialize())
    except Exception as e:
        db.session.rollback()
        return jsonify({"error" : str(e)}) , 500

@modelli_f24_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_modello_f24(id):
    modello_f24 = ModelloF24.query.get_or_404(id)
    db.session.delete(modello_f24)
    db.session.commit()
    return '', 204

@modelli_f24_blueprint.route('/<int:id>/prepara', methods=['GET'])
def prepara_modello_f24(id):
    modello_f24 = ModelloF24.query.get_or_404(id)
    return modello_f24.prepara_f24()