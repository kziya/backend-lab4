from flask import jsonify, request
from marshmallow import ValidationError

from src import app
from src.auth.auth_service import AuthService
from src.auth.register_and_login_schema import RegisterAndLoginSchema

authService = AuthService()


@app.route('/auth/register', methods=['POST'])
def register():
    try:
        requestBody = request.get_json()
        RegisterAndLoginSchema().load(data=requestBody)
        return authService.registerUser(email=requestBody.get('email'), name=requestBody.get('name'),
                                        password=requestBody.get('password'))
    except ValidationError as err:
        return jsonify({'message': err.messages})


@app.route('/auth/login', methods=['POST'])
def login():
    try:
        requestBody = request.get_json()
        RegisterAndLoginSchema().load(data=requestBody)
        return authService.loginUser(email=requestBody.get('email'), password=requestBody.get('password'))
    except ValidationError as e:
        return jsonify({'message': e.messages})
