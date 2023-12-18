from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Str(dump_only=True, required=False)
    name = fields.Str(required=True)
