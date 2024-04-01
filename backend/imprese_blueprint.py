from datetime import datetime
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
    try :
        data = request.json
        comune_id = None
        if ('comune_id' in data.keys()):
            comune_id = data.pop('comune_id')
        impresa = Impresa(**data)
        if (comune_id != None):
            comune = Comune.query.get_or_404(comune_id)
            comune.imprese_registrate.append(impresa)
        db.session.add(impresa)
        db.session.commit()
        return jsonify(impresa.serialize()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error" : str(e)}) , 500

@imprese_blueprint.route('/<int:id>', methods=['PUT'])
def update_impresa(id):
    try:
        impresa = Impresa.query.get_or_404(id)
        data = request.json
        comune_id = data.pop('comune_id')
        if (impresa.comune_id != None):
            comune = Comune.query.get_or_404(impresa.comune_id)
            comune.imprese_registrate.remove(impresa)
        if (comune_id != None):
            comune = Comune.query.get_or_404(comune_id)
            comune.imprese_registrate.append(impresa)
        for key, value in data.items():
            if (key == "data_costituzione"):
                value = datetime.strptime(value, "%Y-%m-%d")
            setattr(impresa, key, value)
        db.session.commit()
        return jsonify(impresa.serialize())
    except Exception as e:
        db.session.rollback()
        return jsonify({"error" : str(e)}) , 500

@imprese_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_impresa(id):
    impresa = Impresa.query.get_or_404(id)
    db.session.delete(impresa)
    db.session.commit()
    return '', 204
