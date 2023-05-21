from flask import request, jsonify

from . import bp
from app.models import User

@bp.route('/verify-user', methods=['POST'])
def verify_user():
    content = request.json
    print(content)
    username= content['username']
    password= content['password']
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return jsonify([{'user token': user.token}])
    
@bp.route('/register-user', methods=['POST'])
def register_user():
    content = request.json
    username= content['username']
    email = content['email']
    password= content['password']
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify[{'message':'Username Taken, Try Again'}]
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify[{'message':'Email Taken, Try Again'}]
    user = User(email=email, username=username)
    user.password = user.hash_password(password)
    user.add_token()
    user.commit()
    print(user)
    return jsonify([{'message': f'{user.username} Registered'}])
