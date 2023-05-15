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