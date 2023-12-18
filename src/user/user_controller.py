from flask import request, jsonify
from marshmallow import ValidationError

from src import app
from src.user.user_schema import UserSchema
from src.user.user_service import UserService

userService = UserService()


@app.route('/user/<int:id>', methods=['GET'])
def getUserById(id):
    return userService.getUserById(id)


@app.route('/user', methods=['POST'])
def addUser():
    try:
        UserSchema().load(data=request.get_json())
        return userService.addUser(request.get_json())
    except ValidationError as err:
        return jsonify({"message": err.messages})


@app.route('/users', methods=['GET'])
def getUsers():
    return userService.getUsers()


@app.route('/user/<int:id>', methods=['DELETE'])
def deleteUser(id):
    return userService.deleteUser(id)
