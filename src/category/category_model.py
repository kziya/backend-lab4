from src import db


class CategoryModel(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    idPrivateUser = db.Column(db.Integer, default=0)

    record = db.relationship('RecordModel', back_populates='category', lazy='dynamic')

    def toDict(self):
        return {
            'id': self.id,
            'name': self.name
        }

    @staticmethod
    def toDictList(array):
        return list(map(lambda x: x.toDict(), array))
