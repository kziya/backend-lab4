class Category:
    def __init__(self, id, name, idPrivateUser):
        self.id = id
        self.name = name
        self.idPrivateUser = idPrivateUser

    def getDict(self):
        return {'id': self.id, 'name': self.name}
