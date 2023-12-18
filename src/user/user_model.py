from src import db


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    record = db.relationship('RecordModel', back_populates='user', lazy='dynamic')

    def toDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }

    @staticmethod
    def toDictList(users):
        return list(map(lambda u: u.toDict(), users))
