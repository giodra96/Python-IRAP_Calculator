from flask import Blueprint, jsonify, request
from models import db, Impresa, Comune, ModelloF24  # Assicurati di importare i modelli necessari

imprese_blueprint = Blueprint('imprese_blueprint', __name__, url_prefix='/api/imprese')

# Gestione delle Imprese
@imprese_blueprint.route('/', methods=['GET'])
def get_all_imprese():
    imprese = Impresa.query.all()
    return jsonify([imp.serialize() for imp in imprese])

@imprese_blueprint.route('/<int:id>', methods=['GET'])
def get_impresa(id):
    impresa = Impresa.query.get_or_404(id)
    return jsonify(impresa.serialize())

@imprese_blueprint.route('/', methods=['POST'])
def create_impresa():
    data = request.json
    impresa = Impresa(**data)
    db.session.add(impresa)
    db.session.commit()
    return jsonify(impresa.serialize()), 201

@imprese_blueprint.route('/<int:id>', methods=['PUT'])
def update_impresa(id):
    impresa = Impresa.query.get_or_404(id)
    data = request.json
    for key, value in data.items():
        setattr(impresa, key, value)
    db.session.commit()
    return jsonify(impresa.serialize())

@imprese_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_impresa(id):
    impresa = Impresa.query.get_or_404(id)
    db.session.delete(impresa)
    db.session.commit()
    return '', 204

# Gestione dei ModelliF24 emessi per una determinata Impresa
@imprese_blueprint.route('/<int:id>/modellif24', methods=['GET'])
def get_modelli_f24_of_impresa(id):
    impresa = Impresa.query.get_or_404(id)
    return jsonify([mf.serialize() for mf in impresa.modelli_f24])

@imprese_blueprint.route('/<int:id>/modellif24', methods=['POST'])
def create_modellif24_for_impresa(id):
    impresa = Impresa.query.get_or_404(id)
    data = request.json
    modello_f24 = ModelloF24(impresa=impresa, **data)
    db.session.add(modello_f24)
    db.session.commit()
    return jsonify(modello_f24.serialize()), 201
