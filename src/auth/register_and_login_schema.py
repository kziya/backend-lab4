from marshmallow import Schema, fields


class RegisterAndLoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    name = fields.Str()
