from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from secrets import token_urlsafe
from app import db,login

@login.user_loader
def load_user(id):
    return User.query.get(id)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_super_hero_name = db.Column(db.String(50))
    username = db.Column(db.String(40), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String)
    collections = db.relationship('UserCollection', backref='author', lazy=True)
    token = db.Column(db.String(250), unique=True)
    

    def __repr__(self):
        return f'User: {self.username}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def hash_password(self,password):
        return generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password, password)
    def add_token(self):
        setattr(self,'token',token_urlsafe(32))
    
    def get_id(self):
        return str(self.id)
    
class UserCollection(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250))
    description = db.Column(db.String(250))
    comics_appeared_in = db.Column(db.Integer)
    super_power = db.Column(db.String(250))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"UserCollection {self.name} {self.description} {self.comics_appeared_in} {self.super_power}"
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
