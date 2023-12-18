from src import db
from src.user.user_model import UserModel


class UserRepository:
    _users = []

    def addUser(self, name):
        newUser = UserModel(name=name)
        db.session.add(newUser)
        db.session.commit()

    def removeUserById(self, id):
        userToRemove = UserModel.query.get(id)
        if userToRemove is not None:
            db.session.delete(userToRemove)
            db.session.commit()

        return True

    def getAllUsers(self):
        return UserModel.toDictList(UserModel.query.all())

    def getUserById(self, id):
        user = UserModel.query.get(id)
        if user is not None:
            return user

        return None


userRepository = UserRepository()
