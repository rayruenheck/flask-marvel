from flask import request, jsonify

from . import bp
from app.models import UserCollection, User

from app.blueprints.api.helpers import token_required


@bp.route('/collections/<username>', methods=['GET'])
@token_required
def user_collections(user, username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify([{'id':user.id, 'name':user.name, 'desciption': user.description, 'comics appeared in': user.comics, 'superpower': user.superpower}])
    return jsonify({'message': 'Invalid Username'}), 404

@bp.route('/collection/<collection_id>', methods=['GET'])
@token_required
def get_collection(user,collection_id):
    try:
        collection = UserCollection.query.get(collection_id)
        return jsonify([{'id': collection.id, 'name': collection.name, 'description': collection.description, 'comics_appeared_in': collection.comics_appeared_in,'super_power': collection.super_power,'timestamp':collection.timestamp, 'author':collection.user_id}])
    except:
        return({'message':'Invalid Username'}), 404

@bp.route('/collection',methods=['POST'])
@token_required
def make_collection(user):
    try:
        content = request.json
        collection = UserCollection(name=content.get('name'),description=content.get('description'),super_power=content.get('super_power'),comics_appeared_in=content.get('comics_appeared_in'), user_id=user.user_id)
        collection.commit()
        return jsonify([{'message':'collection created','name': collection.name, 'description': collection.description, 'comics_appeared_in': collection.comics_appeared_in,'super_power': collection.super_power}])
    except:
        jsonify([{'message': 'Inavalid form data'}])