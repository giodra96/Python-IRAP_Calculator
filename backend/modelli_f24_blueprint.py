from flask import Blueprint, jsonify, request
from models import db, ModelloF24, Impresa, Comune  # Assicurati di importare i modelli necessari

modelli_f24_blueprint = Blueprint('modelli_f24_blueprint', __name__, url_prefix='/api/modellif24')

# Gestione dei ModelliF24
@modelli_f24_blueprint.route('', methods=['GET'])
def get_all_modellif24():
    modellif24 = ModelloF24.query.all()
    return jsonify([mf.serialize() for mf in modellif24])

@modelli_f24_blueprint.route('/<int:id>', methods=['GET'])
def get_modellif24(id):
    modellif24 = ModelloF24.query.get_or_404(id)
    return jsonify(modellif24.serialize())

@modelli_f24_blueprint.route('/<int:id>', methods=['POST'])
def create_modellif24():
    data = request.json
    impresa_id = data.get('impresa_id')
    impresa = Impresa.query.get_or_404(impresa_id)
    modellif24 = ModelloF24(impresa=impresa, **data)
    db.session.add(modellif24)
    db.session.commit()
    return jsonify(modellif24.serialize()), 201

@modelli_f24_blueprint.route('/<int:id>', methods=['PUT'])
def update_modellif24(id):
    modellif24 = ModelloF24.query.get_or_404(id)
    data = request.json
    for key, value in data.items():
        setattr(modellif24, key, value)
    db.session.commit()
    return jsonify(modellif24.serialize())

@modelli_f24_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_modellif24(id):
    modellif24 = ModelloF24.query.get_or_404(id)
    db.session.delete(modellif24)
    db.session.commit()
    return '', 204
