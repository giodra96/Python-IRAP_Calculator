from flask import Blueprint, jsonify, request
from models import db, Comune

comuni_blueprint = Blueprint('comuni_blueprint', __name__, url_prefix='/api/comuni')

# Gestione dei Comuni
@comuni_blueprint.route('/', methods=['GET'])
def get_all_comuni():
    data = request.args
    comuni = []
    if ('nome' in data.keys()):
        comuni = Comune.query.filter_by(nome=data.get('nome'))
    else:
        comuni = Comune.query.all()
    return jsonify([c.serialize() for c in comuni])

@comuni_blueprint.route('/<int:id>', methods=['GET'])
def get_comune(id):
    comune = Comune.query.get_or_404(id)
    return jsonify(comune.serialize())

@comuni_blueprint.route('/', methods=['POST'])
def create_comune():
    try :
        data = request.json
        comune = Comune(**data)
        db.session.add(comune)
        db.session.commit()
        return jsonify(comune.serialize()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error" : str(e)}) , 500

@comuni_blueprint.route('/<int:id>', methods=['PUT'])
def update_comune(id):
    try :
        comune = Comune.query.get_or_404(id)
        data = request.json
        if ('id' in data.keys()):
            return { "error" : "Change id not possible" }, 404
        for key, value in data.items():
            setattr(comune, key, value)
        db.session.commit()
        return jsonify(comune.serialize())
    except Exception as e:
        db.session.rollback()
        return jsonify({"error" : str(e)}) , 500

@comuni_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_comune(id):
    comune = Comune.query.get_or_404(id)
    db.session.delete(comune)
    db.session.commit()
    return '', 204