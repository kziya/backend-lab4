from flask import jsonify
from flask_jwt_extended import create_access_token
from passlib.handlers.pbkdf2 import pbkdf2_sha256

from src import db
from src.user.user_model import UserModel


class AuthService:
    def registerUser(self, email, password, name):
        user = UserModel.query.filter_by(email=email).first()

        if user is not None:
            return jsonify({'message': 'Email already registered'}), 400

        user = UserModel(email=email, name=name, password=pbkdf2_sha256.hash(password))

        db.session.add(user)
        db.session.commit()

        return jsonify({'accessToken': create_access_token(identity=user.id), 'id': user.id}), 200

    def loginUser(self, email, password):
        user = UserModel.query.filter_by(email=email).first()
        if user and pbkdf2_sha256.verify(password, user.toDict().get('password')):
            return jsonify({'accessToken': create_access_token(user.id)}), 200

        return jsonify({'message': 'Email or password incorrect'}), 400
