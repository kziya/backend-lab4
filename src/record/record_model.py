from src import db


class RecordModel(db.Model):
    __tablename__ = 'record'

    id = db.Column(db.Integer, primary_key=True)
    idUser = db.Column(db.Integer, db.ForeignKey('user.id'))
    idCategory = db.Column(db.Integer, db.ForeignKey('category.id'))
    expenditureAmount = db.Column(db.Float)

    user = db.relationship('UserModel', backref='user')
    category = db.relationship('CategoryModel', backref='category')

    def toDict(self):
        return {
            'id': self.id,
            'idUser': self.idUser,
            'idCategory': self.idCategory,
            'expenditureAmount': self.expenditureAmount
        }

    @staticmethod
    def toDictList(records):
        return list(map(lambda r: r.toDict(), records))
