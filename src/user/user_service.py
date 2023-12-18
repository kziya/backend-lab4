from flask import jsonify

from src.user.user_repository import userRepository


class UserService:
    def getUserById(self, id):
        user = userRepository.getUserById(id)
        if user is None:
            return jsonify({'message': 'User is not found !'}), 404
        return jsonify(user), 200

    def addUser(self, requestBody):
        name = requestBody.get('name')
        if name is None:
            return jsonify({'message': 'Bad request !'}), 400
        addResult = userRepository.addUser(name)
        return jsonify(addResult), 200

    def getUsers(self):
        return userRepository.getAllUsers()

    def deleteUser(self, id):
        removeResult = userRepository.removeUserById(id)
        return jsonify({'result': removeResult}), 200
