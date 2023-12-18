from flask import jsonify

from src.category.category_repository import categoryRepository
from src.record.record_repository import recordRepository
from src.user.user_repository import userRepository


class RecordService:
    def addRecord(self, requestBody):
        idUser = requestBody.get('idUser')
        user = userRepository.getUserById(idUser)

        if user is None:
            return jsonify({'message': 'User is not found !'}), 404

        idCategory = requestBody.get('idCategory')
        category = categoryRepository.getCategoryById(idCategory)

        if category is None:
            return jsonify({'message': 'Category is not found !'}), 404

        expenditureAmount = requestBody.get('expenditureAmount')
        if expenditureAmount < 1:
            return jsonify({'message': 'Expenditure amount can not be less than 1 !'}), 400

        addResult = recordRepository.addRecord(idUser, idCategory, expenditureAmount)
        return jsonify(addResult), 201

    def getRecordById(self, id):
        record = recordRepository.getRecordById(id)
        if record is None:
            return jsonify({'message': 'Record is not found !'}), 404
        return jsonify(record), 200

    def removeRecordById(self, id):
        removeResult = recordRepository.removeRecordById(id)
        if not removeResult:
            return jsonify({'message': 'Record is not found !'}), 404

        return jsonify({'result': removeResult}), 200

    def getRecords(self, requestBody):
        idUser = requestBody.get('idUser')
        idCategory = requestBody.get('idCategory')
        if not idUser and not idCategory:
            return jsonify({'message': 'Bad request !'}), 400
        records = recordRepository.getRecords(requestBody.get('idUser'), requestBody.get('idCategory'))
        return jsonify(records), 200
