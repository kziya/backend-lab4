from flask import request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError

from src import app
from src.record.record_model import RecordModel
from src.record.record_schema import RecordSchema
from src.record.record_service import RecordService

recordService = RecordService()


@app.route('/record/all', methods=['GET'])
@jwt_required()
def getAllRecords():
    return RecordModel.toDictList(RecordModel.query.all())


@app.route('/record', methods=['POST'])
@jwt_required()
def addRecord():
    try:
        RecordSchema().load(data=request.get_json())
        return recordService.addRecord(request.get_json())
    except ValidationError as err:
        return jsonify({"message": err.messages})


@app.route('/record/<int:id>', methods=['GET'])
@jwt_required()
def getRecordById(id):
    return recordService.getRecordById(id)


@app.route('/record', methods=['GET'])
@jwt_required()
def getRecords():
    return recordService.getRecords(request.get_json())
