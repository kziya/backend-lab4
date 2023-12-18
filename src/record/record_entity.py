import datetime


class Record:
    def __init__(self, id, idUser, idCategory, expenditureAmount):
        self.id = id
        self.idUser = idUser
        self.idCategory = idCategory
        self.expenditureAmount = expenditureAmount
        self.dateCreated = datetime.datetime.now()

    def getDict(self):
        return {
            'id': self.id,
            'idUser': self.idUser,
            'idCategory': self.idCategory,
            'expenditureAmount': self.expenditureAmount,
            'dateCreated': str(self.dateCreated)
        }
