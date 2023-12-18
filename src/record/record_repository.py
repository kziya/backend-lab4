from src import db
from src.record.record_model import RecordModel


class RecordRepository:
    _records = []

    def addRecord(self, idUser, idCategory, expenditureAmount):
        record = RecordModel(idUser=idUser, idCategory=idCategory, expenditureAmount=expenditureAmount)
        db.session.add(record)
        db.session.commit()

        return record.toDict()

    def removeRecordById(self, id):
        recordToRemove = RecordModel.query.get(id)

        if recordToRemove is not None:
            db.session.delete(recordToRemove)
            db.session.commit()

        return True

    def getRecordById(self, id):
        record = RecordModel.query.get(id)

        if record is not None:
            return record.toDict()

        return None

    def getRecords(self, id_user, id_category):
        query = RecordModel.query

        if id_user is not None and id_category is not None:
            # Both id_user and id_category are provided
            query = query.filter(RecordModel.idUser == id_user, RecordModel.idCategory == id_category)
        elif id_user is not None:
            # Only id_user is provided
            query = query.filter(RecordModel.idUser == id_user)
        elif id_category is not None:
            # Only id_category is provided
            query = query.filter(RecordModel.idCategory == id_category)

        # Execute the query
        records = query.all()

        return RecordModel.toDictList(records)


recordRepository = RecordRepository()
