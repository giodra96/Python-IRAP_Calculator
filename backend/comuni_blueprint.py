from flask import Blueprint, jsonify, request
from models import db, Comune, Impresa, ModelloF24  # Assicurati di importare i modelli necessari

comuni_blueprint = Blueprint('comuni_blueprint', __name__, url_prefix='/api/comuni')

# Gestione dei Comuni
@comuni_blueprint.route('/', methods=['GET'])
def get_all_comuni():
    comuni = Comune.query.all()
    return jsonify([c.serialize() for c in comuni])

@comuni_blueprint.route('/<int:id>', methods=['GET'])
def get_comune(id):
    comune = Comune.query.get_or_404(id)
    return jsonify(comune.serialize())

@comuni_blueprint.route('/', methods=['POST'])
def create_comune():
    data = request.json
    comune = Comune(**data)
    db.session.add(comune)
    db.session.commit()
    return jsonify(comune.serialize()), 201

@comuni_blueprint.route('/<int:id>', methods=['PUT'])
def update_comune(id):
    comune = Comune.query.get_or_404(id)
    data = request.json
    for key, value in data.items():
        setattr(comune, key, value)
    db.session.commit()
    return jsonify(comune.serialize())

@comuni_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_comune(id):
    comune = Comune.query.get_or_404(id)
    db.session.delete(comune)
    db.session.commit()
    return '', 204

# Gestione delle Imprese associate a un Comune
@comuni_blueprint.route('/<int:id>/imprese', methods=['GET'])
def get_imprese_of_comune(id):
    comune = Comune.query.get_or_404(id)
    return jsonify([imp.serialize() for imp in comune.imprese_registrate])

@comuni_blueprint.route('/<int:id>/imprese', methods=['POST'])
def create_impresa_for_comune(id):
    comune = Comune.query.get_or_404(id)
    data = request.json
    impresa = Impresa(**data)
    comune.imprese_registrate.append(impresa)
    db.session.commit()
    return jsonify(impresa.serialize()), 201

# Gestione dei ModelliF24 emessi da un Comune per una determinata Impresa
@comuni_blueprint.route('/<int:id_comune>/imprese/<int:id_impresa>/modellif24', methods=['GET'])
def get_modelli_f24_of_impresa(id_comune, id_impresa):
    comune = Comune.query.get_or_404(id_comune)
    modelli_f24 = [mf.serialize() for mf in comune.modelli_f24_emessi if mf.impresa_id == id_impresa]
    return jsonify(modelli_f24)

@comuni_blueprint.route('/<int:id_comune>/imprese/<int:id_impresa>/modellif24', methods=['POST'])
def create_modellif24_for_impresa(id_comune, id_impresa):
    comune = Comune.query.get_or_404(id_comune)
    impresa = Impresa.query.get_or_404(id_impresa)
    data = request.json
    modello_f24 = ModelloF24(impresa=impresa, **data)
    comune.modelli_f24_emessi.append(modello_f24)
    db.session.commit()
    return jsonify(modello_f24.serialize()), 201
