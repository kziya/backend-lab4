from marshmallow import Schema, fields


class CategorySchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class PrivateCategorySchema(CategorySchema):
    idPrivateUser = fields.Integer(required=True)
