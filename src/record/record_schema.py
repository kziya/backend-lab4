from marshmallow import Schema, fields


class RecordSchema(Schema):
    id = fields.Str(dump_only=True)
    idUser = fields.Str(required=True)
    idCategory = fields.Str(required=True)
    expenditureAmount = fields.Float(required=True)
